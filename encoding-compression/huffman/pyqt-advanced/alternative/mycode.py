import sys
import os
import pickle
import heapq
from collections import Counter
import networkx as nx
import matplotlib.pyplot as plt
from tabulate import tabulate
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                             QHBoxLayout, QPushButton, QLabel, QLineEdit,
                             QFileDialog, QComboBox, QMessageBox, QFrame,
                             QGroupBox, QTextBrowser)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont


class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
        self.code = ""

    def __lt__(self, other):
        if not isinstance(other, Node):
            return NotImplemented
        return self.freq < other.freq


def build_huffman_tree(text):
    frequency = Counter(text)
    total_chars = len(text)
    heap = [Node(char, freq / total_chars) for char, freq in frequency.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0]


def generate_huffman_codes(node, current_code="", codes={}):
    if node is None:
        return

    node.code = current_code

    if node.char is not None:
        codes[node.char] = current_code
    generate_huffman_codes(node.left, current_code + "0", codes)
    generate_huffman_codes(node.right, current_code + "1", codes)
    return codes


def huffman_encode(text):
    root = build_huffman_tree(text)
    huffman_codes = generate_huffman_codes(root)
    encoded_text = ''.join([huffman_codes[char] for char in text])
    root.codes = huffman_codes
    return encoded_text, root


def huffman_decode(encoded_text, root):
    decoded_text = []
    node = root
    for bit in encoded_text:
        node = node.left if bit == '0' else node.right
        if node.char is not None:
            decoded_text.append(node.char)
            node = root
    return ''.join(decoded_text)


def format_huffman_codes(codes):
    table_data = []
    for char, code in sorted(codes.items()):
        char_display = 'ПРОБЕЛ' if char == ' ' else char
        table_data.append([char_display, code, len(code)])

    headers = ['Символ', 'Код', 'Длина кода']
    table = tabulate(table_data, headers=headers, tablefmt='grid')

    frequency = Counter(''.join(str(char) * len(code)
                        for char, code in codes.items()))
    total_bits = sum(len(codes[char]) * freq for char,
                     freq in frequency.items())
    total_chars = sum(frequency.values())
    avg_code_length = total_bits / total_chars if total_chars > 0 else 0

    stats = (
        f"\n\nСтатистика кодирования:"
        f"\nОбщее количество символов: {total_chars}"
        f"\nОбщее количество бит: {total_bits}"
        f"\nСредняя длина кода: {avg_code_length:.2f} бит"
    )

    return table + stats


class HuffmanGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Кодирование Хаффмана')
        self.setMinimumSize(800, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        # Группа для выбора файлов
        files_group = QGroupBox("Файлы")
        files_layout = QVBoxLayout()

        input_layout = QHBoxLayout()
        self.input_file = QLineEdit()
        self.input_file.setPlaceholderText("Путь к входному файлу...")
        input_browse = QPushButton("Обзор")
        input_browse.clicked.connect(self.choose_input_file)
        input_layout.addWidget(QLabel("Входной файл:"))
        input_layout.addWidget(self.input_file)
        input_layout.addWidget(input_browse)

        tree_layout = QHBoxLayout()
        self.tree_file = QLineEdit()
        self.tree_file.setPlaceholderText("Путь к файлу дерева...")
        tree_browse = QPushButton("Обзор")
        tree_browse.clicked.connect(self.choose_tree_file)
        tree_layout.addWidget(QLabel("Файл дерева:"))
        tree_layout.addWidget(self.tree_file)
        tree_layout.addWidget(tree_browse)

        files_layout.addLayout(input_layout)
        files_layout.addLayout(tree_layout)
        files_group.setLayout(files_layout)

        # Группа для действий
        actions_group = QGroupBox("Действия")
        actions_layout = QHBoxLayout()

        self.action_combo = QComboBox()
        self.action_combo.addItems(["Кодировать", "Декодировать"])

        process_button = QPushButton("Выполнить")
        visualize_button = QPushButton("Визуализировать дерево")
        process_button.clicked.connect(self.perform_action)
        visualize_button.clicked.connect(self.visualize_tree)

        actions_layout.addWidget(self.action_combo)
        actions_layout.addWidget(process_button)
        actions_layout.addWidget(visualize_button)
        actions_group.setLayout(actions_layout)

        # Область для вывода результатов
        results_group = QGroupBox("Результаты")
        results_layout = QVBoxLayout()

        self.results_browser = QTextBrowser()
        self.results_browser.setFont(QFont("Courier New", 10))

        results_layout.addWidget(self.results_browser)
        results_group.setLayout(results_layout)

        main_layout.addWidget(files_group)
        main_layout.addWidget(actions_group)
        main_layout.addWidget(results_group)

    def choose_input_file(self):
        filename, _ = QFileDialog.getOpenFileName(
            self,
            "Выберите файл",
            "",
            "Text files (*.txt);;All files (*.*)"
        )
        if filename:
            self.input_file.setText(filename)

    def choose_tree_file(self):
        filename, _ = QFileDialog.getOpenFileName(
            self,
            "Выберите файл дерева",
            "",
            "Huffman Tree files (*.pkl);;All files (*.*)"
        )
        if filename:
            self.tree_file.setText(filename)

    def show_error(self, message):
        QMessageBox.critical(self, "Ошибка", message)

    def show_success(self, message):
        QMessageBox.information(self, "Успех", message)

    def build_networkx_tree(self, node, G=None, parent_id=None, node_id=0, edge_label=""):
        if G is None:
            G = nx.Graph()

        current_id = node_id
        probability = node.freq

        label = f"'{node.char}'\np={probability:.3f}\nКод: {
            node.code}" if node.char is not None else f"p={probability:.3f}\nКод: {node.code}"
        G.add_node(current_id, label=label)

        if parent_id is not None:
            G.add_edge(parent_id, current_id, label=edge_label)

        next_id = current_id + 1
        if node.left:
            next_id = self.build_networkx_tree(
                node.left, G, current_id, next_id, "0")
        if node.right:
            next_id = self.build_networkx_tree(
                node.right, G, current_id, next_id, "1")

        return next_id

    def hierarchy_pos(self, G, root):
        def _hierarchy_pos(G, root, width=1., vert_gap=0.2, vert_loc=0, xcenter=0.5, pos=None, parent=None, parsed=[]):
            if pos is None:
                pos = {root: (xcenter, vert_loc)}
            else:
                pos[root] = (xcenter, vert_loc)
            children = list(G.neighbors(root))
            if parent is not None:
                children.remove(parent)
            if len(children) != 0:
                dx = width / len(children)
                nextx = xcenter - width / 2 - dx / 2
                for child in children:
                    nextx += dx
                    pos = _hierarchy_pos(G, child, width=dx, vert_gap=vert_gap,
                                         vert_loc=vert_loc - vert_gap, xcenter=nextx, pos=pos,
                                         parent=root, parsed=parsed)
            return pos

        return _hierarchy_pos(G, root, width=2., vert_gap=0.4)

    def visualize_tree(self):
        tree_filename = self.tree_file.text()
        if not tree_filename:
            self.show_error("Выберите файл дерева Хаффмана")
            return

        try:
            with open(tree_filename, 'rb') as tree_file:
                tree = pickle.load(tree_file)

            huffman_codes = generate_huffman_codes(tree)
            table = format_huffman_codes(huffman_codes)
            self.results_browser.setText(table)

            G = nx.Graph()
            self.build_networkx_tree(tree, G)

            plt.figure(figsize=(15, 10))
            pos = self.hierarchy_pos(G, 0)

            nx.draw_networkx_nodes(
                G, pos, node_color='lightblue', node_size=3000, alpha=0.9)
            nx.draw_networkx_edges(
                G, pos, edge_color='gray', width=2.0, alpha=0.5)
            labels = nx.get_node_attributes(G, 'label')
            nx.draw_networkx_labels(
                G, pos, labels, font_size=8, font_family='sans-serif')
            edge_labels = nx.get_edge_attributes(G, 'label')
            nx.draw_networkx_edge_labels(
                G, pos, edge_labels, font_size=10, font_weight='bold')

            plt.title("Дерево Хаффмана", pad=20)
            plt.axis('off')
            plt.tight_layout()
            plt.margins(x=0.2, y=0.2)
            plt.show()

        except Exception as e:
            self.show_error(f"Ошибка при визуализации: {str(e)}")

    def perform_action(self):
        filename = self.input_file.text()
        if not filename:
            self.show_error("Выберите файл")
            return

        try:
            with open(filename, 'r', encoding='utf-8') as file:
                text = file.read()
        except Exception as e:
            self.show_error(f"Ошибка при чтении файла: {str(e)}")
            return

        base_name, file_extension = os.path.splitext(filename)
        action = self.action_combo.currentText()

        try:
            if action == "Кодировать":
                encoded_text, tree = huffman_encode(text)
                huffman_codes = generate_huffman_codes(tree)
                table = format_huffman_codes(huffman_codes)
                self.results_browser.setText(table)

                output_file = f"{base_name}_encoded{file_extension}"
                tree_file = f"{base_name}_tree.pkl"

                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(encoded_text)
                with open(tree_file, 'wb') as f:
                    pickle.dump(tree, f)

                self.show_success(
                    f"Файл закодирован: {output_file}\n"
                    f"Дерево сохранено: {tree_file}"
                )

            else:  # Декодирование
                tree_filename = self.tree_file.text()
                if not tree_filename:
                    self.show_error("Выберите файл дерева")
                    return

                with open(tree_filename, 'rb') as f:
                    tree = pickle.load(f)

                decoded_text = huffman_decode(text, tree)
                output_file = f"{base_name}_decoded{file_extension}"

                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(decoded_text)

                self.show_success(f"Файл декодирован: {output_file}")

        except Exception as e:
            self.show_error(f"Ошибка при обработке: {str(e)}")


def main():
    app = QApplication(sys.argv)
    window = HuffmanGUI()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
