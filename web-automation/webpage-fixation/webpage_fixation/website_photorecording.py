from package.website_screenshots_creation_module import take_screenshots_from_website
from package.pdf_report_creation_module import create_website_photorecording_pdf_report
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter.ttk import Progressbar
import threading


def create_gui():
    window = tk.Tk()
    window.title("Веб фиксация вебсайта")
    window.geometry("1280x720")

    url_label = tk.Label(window, text="Введите URL:", font=("Calibri", 18))
    url_label.pack(pady=10)
    url_var = tk.StringVar()
    url_entry = tk.Entry(window, textvariable=url_var,
                         font=("Calibri", 18), width=30)
    url_entry.pack(pady=10)

    def start_button_callback():
        url = url_var.get()
        if not url:
            messagebox.showerror("Ошибка", "Необходимо ввести URL")
        elif not screenshots_file_path_var.get():
            messagebox.showerror(
                "Ошибка", "Необходимо выбрать путь для сохранения файлов")
        else:
            start_main_thread(
                url_var.get(), screen_resolution_var.get(), screenshots_file_path_var.get(), remove_screenshots_var.get(), progressbar)

    screen_resolution_label = tk.Label(
        window, text="Выберите разрешение экрана:", font=("Calibri", 18))
    screen_resolution_label.pack(pady=10)
    screen_resolution_var = tk.StringVar(value="1920x1080")
    screen_resolution_options = ["1920x1080",
                                 "1280x720", "800x600", "640x480", "1360x768"]
    screen_resolution_menu = tk.OptionMenu(
        window, screen_resolution_var, *screen_resolution_options)
    screen_resolution_menu.config(font=("Calibri", 18))
    screen_resolution_menu.pack(pady=10)

    screenshots_file_path_label = tk.Label(
        window, text="Выберите путь для сохранения всех файлов:", font=("Calibri", 18))
    screenshots_file_path_label.pack(pady=10)
    screenshots_file_path_var = tk.StringVar()
    screenshots_file_path_entry = tk.Entry(
        window, textvariable=screenshots_file_path_var, font=("Calibri", 18), width=30)
    screenshots_file_path_entry.pack(pady=10)
    screenshots_file_path_button = tk.Button(window, text="Выбрать", command=lambda: screenshots_file_path_var.set(
        filedialog.askdirectory(initialdir="/", title="Select directory")), font=("Calibri", 18), width=15)
    screenshots_file_path_button.pack(pady=10)

    remove_screenshots_label = tk.Label(
        window, text="Удалить скриншоты после создания отчета?", font=("Calibri", 18))
    remove_screenshots_label.pack(pady=10)
    remove_screenshots_var = tk.StringVar(value="Нет")
    remove_screenshots_options = ["Нет", "Да"]
    remove_screenshots_menu = tk.OptionMenu(
        window, remove_screenshots_var, *remove_screenshots_options)
    remove_screenshots_menu.config(font=("Calibri", 18))
    remove_screenshots_menu.pack(pady=10)

    progressbar = Progressbar(window, length=300, mode="determinate")
    progressbar.pack(pady=10)

    start_button = tk.Button(
        window, text="Начать", command=start_button_callback, font=("Calibri", 18), width=15)
    start_button.pack(pady=10)

    window.mainloop()


def start_main_thread(url, screen_resolution, screenshots_file_path, remove_screenshots, progressbar):
    if screenshots_file_path:
        thread = threading.Thread(target=start_main, args=(
            url, screen_resolution, screenshots_file_path, remove_screenshots, progressbar))
        thread.start()
    else:
        messagebox.showerror("Ошибка", "Не выбран путь для сохранения")


def start_main(url, screen_resolution, screenshots_file_path, remove_screenshots, progressbar):
    progressbar["value"] = 0
    screenshots = take_screenshots_from_website(
        url, screenshots_file_path, screen_resolution, progressbar)
    progressbar["value"] = 50
    create_website_photorecording_pdf_report(progressbar,
                                             screenshots=screenshots, url=url, pdf_report_file_path=screenshots_file_path + r"\website_photorecording.pdf")
    progressbar["value"] = 100
    messagebox.showinfo("Веб фиксация", "Вебсайт зафиксирован. Готово!")
    if remove_screenshots == "Да":
        remove_recently_created_screenshots(screenshots_file_path)


def remove_recently_created_screenshots(path):
    import os
    for file in os.listdir(path):
        if file.startswith("screenshot_"):
            os.remove(os.path.join(path, file))
    messagebox.showinfo("Удаление скриншотов", "Скриншоты удалены.")


def create_photorecording(url, screen_resolution, output_path, progressbar):
    """Create a photorecording of the website"""
    screenshots = take_screenshots_from_website(
        url, output_path, screen_resolution, progressbar)
    create_website_photorecording_pdf_report(progressbar,
                                             screenshots=screenshots, url=url, pdf_report_file_path=output_path + r"\website_photorecording.pdf")
    print(f"PDF report created for {url} to {output_path}.")


if __name__ == "__main__":
    create_gui()
