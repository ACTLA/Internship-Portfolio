# 🎓 Engineering Portfolio

[![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)](https://www.python.org/)
[![C#](https://img.shields.io/badge/C%23-.NET%206+-512BD4.svg)](https://dotnet.microsoft.com/)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)]()

> **Полноценная коллекция проектов** по разработке программного обеспечения, криптографии, компьютерному зрению, сетевому программированию и алгоритмам. Разработано в рамках обучения по направлению **«Информационная безопасность»** и направлению **«Фундаментальная информатика и информационные технологии»**, профиль **«Интеллектуальный анализ данных»**.

--- 

## 📋 Оглавление

<details>
<summary><b>Нажмите, чтобы развернуть</b></summary>

- [📁 Структура репозитория](#-структура-репозитория)
- [🔍 Детальное описание проектов](#-детальное-описание-проектов)
  - [1. Computer Vision](#1-computer-vision-компьютерное-зрение)
  - [2. Cryptography](#2-cryptography-криптография)
  - [3. Encoding & Compression](#3-encoding--compression-кодирование-и-сжатие)
  - [4. Network Programming](#4-network-programming-сетевое-программирование)
  - [5. Web Automation](#5-web-automation-веб-автоматизация)
  - [6. Algorithms & Data Structures](#6-algorithms--data-structures-алгоритмы-и-структуры-данных)
  - [7. Numerical Methods](#7-numerical-methods-численные-методы)
  - [8. Information Theory](#8-information-theory-теория-информации)
- [📦 Archive](#-archive-архивные-проекты)
- [🛠️ Технологический стек](#-технологический-стек)
- [🚀 Быстрый старт](#-быстрый-старт)
- [📊 Статистика репозитория](#-статистика-репозитория)
- [📬 Контакты](#-контакты)

</details>

---

## 📁 Структура репозитория

```
📦 Internship-Portfolio
├── 📂 computer-vision/           # Компьютерное зрение
│   └── 📂 face-recognition-system/
├── 📂 cryptography/              # Криптография и протоколы безопасности
│   ├── 📂 modern-crypto/         # RSA, ElGamal, ГОСТ
│   ├── 📂 protocols/             # SKID3, мессенджеры, нотариат
│   ├── 📂 classical-ciphers/     # Аффинный шифр, перестановки
│   ├── 📂 hash-functions/        # CRC, хеширование
│   └── 📂 cryptanalysis/         # Криптоанализ
├── 📂 encoding-compression/      # Кодирование и сжатие данных
│   ├── 📂 huffman/               # Алгоритм Хаффмана
│   ├── 📂 shannon-fano/          # Алгоритм Шеннона-Фано
│   ├── 📂 arithmetic-coding/     # Арифметическое кодирование
│   ├── 📂 lz-algorithms/         # LZ77, LZ78, LZW
│   ├── 📂 error-correcting/      # Хэмминг, Рид-Соломон
│   └── 📂 encoding-converters/   # Конвертеры кодировок
├── 📂 network-programming/       # Сетевое программирование
│   ├── 📂 socket-examples/       # Базовые сокеты
│   ├── 📂 secure-chat/           # Защищённые чаты
│   └── 📂 mitm-simulations/      # MITM-атаки (образовательные)
├── 📂 web-automation/            # Веб-автоматизация
│   ├── 📂 web-saver/             # Сохранение веб-страниц
│   └── 📂 webpage-fixation/      # Фиксация веб-страниц с отчётами
├── 📂 algorithms-data-structures/# Алгоритмы и структуры данных
│   ├── 📂 sorting/               # Сортировки
│   ├── 📂 stacks-queues/         # Стеки и очереди
│   └── 📂 graphs/                # Графовые алгоритмы
├── 📂 numerical-methods/         # Численные методы
│   ├── 📂 linear-algebra/        # Линейная алгебра
│   ├── 📂 interpolation/         # Интерполяция
│   ├── 📂 integration/           # Интегрирование и ОДУ
│   └── 📂 scilab-labs/           # Лабораторные в Scilab
├── 📂 information-theory/        # Теория информации
│   └── 📂 entropy-calculators/   # Калькуляторы энтропии
├── 📂 docs/                      # Документация
├── 📂 archive/                   # Архивные проекты
├── 📄 requirements.txt           # Зависимости Python
└── 📄 README.md                  # Этот файл
```

---

## 🔍 Детальное описание проектов

### 1. Computer Vision (Компьютерное зрение)

#### 🎭 **Face Recognition System** 
📁 `computer-vision/face-recognition-system/`

Полнофункциональная система биометрической идентификации на основе распознавания лиц с модулем аудита безопасности.

**🏗️ Архитектура:**
```
face-recognition-system/
├── 📄 main.py                 # Точка входа
├── 📄 requirements.txt        # Зависимости
├── 📂 config/                 # Конфигурационные файлы
├── 📂 core/                   # Ядро системы
│   ├── 📄 database_manager.py # Работа с БД пользователей
│   ├── 📄 face_engine.py      # Алгоритмы распознавания лиц
│   └── 📄 camera_manager.py   # Управление веб-камерой
├── 📂 gui/                    # Графический интерфейс
│   ├── 📄 main_application.py # Главное окно
│   ├── 📄 recognition_widget.py # Виджет распознавания
│   ├── 📄 management_widget.py  # Управление пользователями
│   └── 📄 audit_widget.py     # Журнал безопасности
├── 📂 audit/                  # Модуль аудита
│   ├── 📄 logger.py           # Запись событий
│   └── 📄 integration.py      # Встраивание в систему
└── 📂 photos/                 # Хранение фотографий
```

**🔧 Технологии:**
| Библиотека | Назначение |
|------------|------------|
| `opencv-python` | Обработка видеопотока, работа с камерой |
| `face_recognition` + `dlib` | Распознавание лиц (CNN-модель) |
| `PyQt5` | Графический интерфейс |
| `SQLite` | Хранение пользователей и событий аудита |
| `cryptography` | Шифрование чувствительных данных |

**✨ Функционал:**
- ✅ Распознавание лиц в реальном времени (до 30 FPS)
- ✅ Регистрация/удаление пользователей с генерацией 128-мерных биометрических отпечатков
- ✅ Система защиты от избыточных срабатываний (cooldown-механизм)
- ✅ Модуль аудита: логирование всех попыток распознавания, операций с БД, системных событий
- ✅ Экспорт отчётов в CSV для соответствия требованиям 152-ФЗ
- ✅ Трёхпанельный интерфейс: видеопоток, список пользователей, журнал событий

**🚀 Запуск:**
```bash
cd computer-vision/face-recognition-system
pip install -r requirements.txt
python main.py
```

**⚙️ Настройка:**
Файл `config/settings.py` содержит параметры:
```python
RECOGNITION_DELAY = 3                    # Задержка между распознаваниями (сек)
UNKNOWN_FACE_DELAY = 5                   # Задержка для неизвестных лиц
FACE_RECOGNITION_CONFIDENCE_THRESHOLD = 0.6  # Порог распознавания
CAMERA_WIDTH, CAMERA_HEIGHT = 640, 480  # Разрешение камеры
```

---

### 2. Cryptography (Криптография)

#### 🔐 **Modern Crypto** 
📁 `cryptography/modern-crypto/`

| Проект | Путь | Описание |
|--------|------|----------|
| **RSA Block Cipher** | `rsa-block/rsa_block_cipher/` | RSA с блочным шифрованием, работа с файлами |
| **RSA Basic** | `rsa-block/rsa_basic/` | Базовая реализация RSA (генерация ключей) |
| **RSA Cryptanalysis** | `rsa-block/rsa_cryptanalysis/` | Криптоанализ: факторизация, атаки на RSA |
| **ElGamal + Signature** | `elgamal/elgamal_signature/` | Шифрование ElGamal + цифровая подпись |
| **GOST R 34.10-94** | `gost-signature/gost_r3410_94/` | ЭЦП по стандарту ГОСТ Р 34.10-94 |
| **Stream Ciphers** | `stream-ciphers/` | Гамма-шифр, LFSR, генераторы ПСЧ |

**📄 Ключевые файлы:**
- `gost_signature_app.py` — PyQt-приложение для подписи файлов по ГОСТ
- `gamma_cipher_encryption.py` — шифрование гаммой с файловым вводом/выводом
- `elgamal_signature/` — генерация и проверка подписи ElGamal

#### 🔗 **Protocols** 
📁 `cryptography/protocols/`

| Проект | Путь | Описание | Протокол |
|--------|------|----------|----------|
| **Secure Messenger (RSA)** | `secure-messenger-rsa/` | Мессенджер с RSA-шифрованием (клиент/сервер) | RSA key exchange |
| **Secure Messenger (Trent)** | `secure-messenger-advanced/secure_messenger_trent/` | Мессенджер с доверенной третьей стороной | Needham-Schroeder-like |
| **SKID3 Protocol** | `skid3/` | Протокол взаимной аутентификации SKID3 | SKID3 |
| **Notary System** | `notary-system/` | Система «Нотариат» для цифровой подписи | RSA-PSS + SHA-256 |
| **Blakley Secret Sharing** | `blakley-secret-sharing/blakley_secret_sharing/` | Схема разделения секрета Блэкли (3 из 3) | Blakley |

**📄 Ключевые файлы:**
```bash
# Сервер ключей и клиенты (Trent-based messenger)
cryptography/protocols/secure-messenger-advanced/secure_messenger_trent/
├── trent.py    # Сервер доверенной третьей стороны
├── alice.py    # Клиент "Алиса"
├── bob.py      # Клиент "Боб"
└── utils.py    # Криптографические утилиты (RSA, сеть, обработка сообщений)
```

#### 🔤 **Classical Ciphers** 
📁 `cryptography/classical-ciphers/`

| Проект | Путь | Описание |
|--------|------|----------|
| **Affine Cipher** | `affine_cipher/` | Аффинный шифр: шифрование/дешифрование/криптоанализ частотным методом |
| **Permutation Cipher** | `permutation_cipher/` | Шифр перестановки с ключом |
| **Feistel Cipher** | `feistel-substitution/` | Сеть Фейстеля с подстановочными S-блоками |

#### 🔢 **Hash Functions** 
📁 `cryptography/hash-functions/`

| Файл | Описание |
|------|----------|
| `crc_main.py` | Реализация CRC с поиском коллизий |
| `crc_lab1.py` – `crc_lab6.py` | Различные лабораторные реализации CRC |

#### 🔍 **Cryptanalysis** 
📁 `cryptography/cryptanalysis/`

| Файл | Описание |
|------|----------|
| `ferma_factorization.py` | Факторизация Ферма для криптоанализа RSA |
| `tasks/` | Задачи для криптоанализа |

---

### 3. Encoding & Compression (Кодирование и сжатие)

#### 🌳 **Huffman Coding** 
📁 `encoding-compression/huffman/`

| Проект | Путь | Описание |
|--------|------|----------|
| **PyQt Advanced** | `pyqt-advanced/` | Хаффман с визуализацией дерева (NetworkX + Matplotlib) |
| **PyQt Basic** | `pyqt-basic/` | Базовая реализация с минималистичным GUI |

**✨ Функционал:**
- Построение дерева Хаффмана на основе частот символов
- Визуализация структуры дерева с вероятностями и кодами
- Шифрование/дешифрование текстовых файлов
- Статистика сжатия: исходный размер, размер после кодирования, коэффициент компрессии

#### 🔀 **Shannon-Fano Coding** 
📁 `encoding-compression/shannon-fano/`

| Проект | Путь | Описание |
|--------|------|----------|
| **CLI** | `cli/` | Консольная версия с параметрами командной строки |

#### 🔢 **Arithmetic Coding** 
📁 `encoding-compression/arithmetic-coding/`

| Проект | Путь | Описание |
|--------|------|----------|
| **PyQt** | `pyqt/` | Арифметическое кодирование с GUI |

#### 🗜️ **LZ Algorithms** 
📁 `encoding-compression/lz-algorithms/`

| Алгоритм | Путь | Описание |
|----------|------|----------|
| **LZ78** | `lz78-pyqt/` | Словарное сжатие LZ78 с динамическим словарём |
| **LZW** | `lzw-cli/` | LZW компрессия (консольная версия) |

#### 🛡️ **Error-Correcting Codes** 
📁 `encoding-compression/error-correcting/`

| Код | Путь | Описание |
|-----|------|----------|
| **Hamming** | `hamming-pyqt/` | Код Хэмминга (7,4) с исправлением одиночных ошибок, визуализация |
| **Reed-Solomon** | `reed-solomon/` | Код Рида-Соломона (32 контрольных символа), исправление пакетных ошибок |

**📄 Ключевые файлы:**
- `hamming_pyqt.py` — PyQt GUI для кодирования/декодирования с подсветкой ошибок
- `reed_solomon_pyqt.py` — кодирование/декодирование с отчётом об исправленных ошибках

#### 🔤 **Encoding Converters** 
📁 `encoding-compression/encoding-converters/`

| Проект | Путь | Описание |
|--------|------|----------|
| **PyQt** | `encoding_converter_pyqt/` | Конвертер кодировок с автоопределением (chardet) |
| **CLI** | `encoding_converter_cli/` | Консольный конвертер для пакетной обработки |

**Поддерживаемые кодировки:** `UTF-8`, `CP866`, `CP1251`, `CP10007 (MacCyrillic)`, `ISO-8859-5`

---

### 4. Network Programming (Сетевое программирование)

#### 🔌 **Socket Examples** 
📁 `network-programming/socket-examples/`

| Файл | Описание |
|------|----------|
| `socket_client.py` | TCP-клиент с цветным логированием |
| `socket_server.py` | Многопоточный TCP-сервер |
| `crypto_operations_gui.py` | GUI для криптографических операций (модульное возведение, НОД, генерация простых) |

#### 🔐 **Secure Chat** 
📁 `network-programming/secure-chat/`

| Проект | Путь | Описание |
|--------|------|----------|
| **Fernet Chat** | `secure_chat_fernet/` | Защищённый чат с шифрованием Fernet, обмен ключами через Трента |
| **C# Messenger** | `messenger_csharp_winforms/` | Мессенджер на C# WinForms с базовым шифрованием |

**📄 Ключевые файлы:**
```bash
secure_chat_fernet/
├── server_trent.py    # Сервер обмена ключами (Трент)
├── client_alice.py    # Клиент "Алиса"
└── client_bob.py      # Клиент "Боб"
```

#### ⚠️ **MITM Simulations** 
📁 `network-programming/mitm-simulations/`

> ⚠️ **ВНИМАНИЕ:** Код предназначен **только для образовательных целей** и тестирования в изолированной среде.

| Проект | Путь | Описание |
|--------|------|----------|
| **ARP Spoofing** | `mitm_arp_spoofing/` | Симуляция ARP-spoofing атаки с перехватом трафика |
| **InfoSec Labs** | `infosec_labs/` | Лабораторные работы по информационной безопасности |

**📄 Файлы лабораторных:**
- `md5_hashing.py` — реализация хеш-функции MD5
- `digital_signature_md5.py` — ЭЦП на основе MD5 + RSA
- `notary.py` — система нотариата с тремя ролями
- `arp_spoofing_tool.py` — симуляция перехвата канала связи

---

### 5. Web Automation (Веб-автоматизация)

#### 💾 **Web Saver** 
📁 `web-automation/web-saver/web_saver/`

| Файл | Описание |
|------|----------|
| `main.py` | Сохранение веб-страниц с использованием Selenium: скриншоты, HTML, PDF-отчёт |

**✨ Функционал:**
- Автоматический скриншот всей страницы (прокрутка + склейка)
- Сохранение исходного HTML-кода
- Генерация PDF-отчёта с метаданными
- Сбор WHOIS-информации о домене

#### 📸 **Webpage Fixation** 
📁 `web-automation/webpage-fixation/webpage_fixation/`

| Файл | Описание |
|------|----------|
| `website_photorecording.py` | Фиксация веб-страниц с генерацией юридически значимого отчёта |
| `package/` | Модули для сбора данных (скриншоты, WHOIS, DNS, трассировка) |

**✨ Функционал:**
- Сбор WHOIS-информации о домене
- Выполнение и запись DNS-трассировки (tracert)
- Создание полноразмерных скриншотов с перекрытием
- Объединение всех данных в единый PDF-документ
- Уникальный номер протокола и временная метка

**🔧 Технологии:**
| Библиотека | Назначение |
|------------|------------|
| `selenium` | Автоматизация браузера (Chrome/Edge) |
| `reportlab` | Генерация PDF-отчётов |
| `beautifulsoup4` | Парсинг HTML-структуры |
| `python-whois` | WHOIS-запросы |
| `Pillow` | Обработка и ресайз скриншотов |

**🚀 Запуск:**
```bash
cd web-automation/webpage-fixation/webpage_fixation
pip install -r requirements.txt
python website_photorecording.py
```

---

### 6. Algorithms & Data Structures (Алгоритмы и структуры данных)

#### 🔢 **Sorting** 
📁 `algorithms-data-structures/sorting/sorting_algorithms/`

| Файл | Описание | Сложность |
|------|----------|-----------|
| `poem_merge_sort.py` | Сортировка слиянием с визуализацией | O(n log n) |
| `poem_quick_sort_hoare.py` | Быстрая сортировка (схема Хоара) | O(n log n) avg |
| `poem_quick_sort_simple.py` | Упрощённая быстрая сортировка | O(n²) worst |

#### 📚 **Stacks & Queues** 
📁 `algorithms-data-structures/stacks-queues/`

| Проект | Путь | Описание |
|--------|------|----------|
| **Calculator** | `stack_calculator/` | Калькулятор на основе стека |
| **Next Greater** | `stack_next_greater/` | Поиск следующего большего элемента |

#### 🗺️ **Graphs** 
📁 `algorithms-data-structures/graphs/graph_bus_path/`

| Файл | Описание | Алгоритм |
|------|----------|----------|
| `bus_path.py` | Поиск оптимального маршрута на графе | Дейкстра / BFS |

---

### 7. Numerical Methods (Численные методы)

#### 🧮 **Linear Algebra** 
📁 `numerical-methods/linear-algebra/`

| Файл | Описание |
|------|----------|
| `f1.py` | Операции с матрицами: умножение, транспонирование |
| `f2.py` | Решение систем линейных уравнений (метод Гаусса) |
| `f3.py` | Вычисление собственных значений и векторов |
| `f4.py` | Метод наименьших квадратов для аппроксимации |
| `approximation_t1.py` – `t3.py` | Аппроксимация: парабола, экспонента, степенная функция |

#### 📈 **Interpolation** 
📁 `numerical-methods/interpolation/`

| Файл | Описание |
|------|----------|
| `four1.py` – `four8.py` | Интерполяционные полиномы, кубические сплайны, B-сплайны, радиальные базисные функции |
| `ode_solving.py` | Решение ОДУ методами Эйлера и Рунге-Кутты |

#### ∫ **Integration** 
📁 `numerical-methods/integration/`

| Файл | Описание |
|------|----------|
| `five1.py`, `five2.py` | Методы трапеций и Симпсона |
| `ode_system.py` | Решение систем ОДУ |
| `six1.py`, `six2.py` | Индивидуальные задания (ОДУ, системы) |

#### 📊 **Scilab Labs** 
📁 `numerical-methods/scilab-labs/scilab_labs/`

| Лабораторная | Описание |
|--------------|----------|
| `Lab-1` – `Lab-2` | Базовые вычисления, построение графиков |
| `Lab-3` | 3D-визуализация функций |
| `Lab-4` | Численное интегрирование |
| `Lab-5` | Решение ОДУ |
| `Lab-6` | Системы линейных уравнений |
| `Lab-7` | Интерполяция и сглаживание |
| `Lab-8` | Статистический анализ |
| `Lab-9` | Межотраслевой баланс |

---

### 8. Information Theory (Теория информации)

#### 📊 **Entropy Calculators** 
📁 `information-theory/entropy-calculators/`

| Проект | Путь | Описание |
|--------|------|----------|
| **Python** | `python/urns_balls_python/` | Калькуляторы энтропии (урны и шары) |
| **Python Advanced** | `python-advanced/` | Цепи Маркова с PyQt-интерфейсом |

**📐 Поддерживаемые формулы:**
- Энтропия Шеннона: `H(X) = -Σ P(x)·log₂P(x)`
- Условная энтропия: `H(Y|X)`
- Совместная энтропия: `H(X,Y)`

---

## 📦 Archive (Архивные проекты)

В папке `archive/` хранятся учебные работы и альтернативные реализации:

| Категория | Содержимое |
|-----------|------------|
| **C# Projects** | `cryptography-csharp-projects/` — проекты на .NET (WinForms, WPF, MAUI) |
| **Deep Learning** | `deep-learning-notes/`, `deep-learning-develop/` — материалы по нейросетям |
| **Encoding Alternatives** | `encoding-compression-alternatives/` — альтернативные реализации алгоритмов |
| **Encoding Converter** | `encoding-converter-csharp/`, `encoding-converter-tutov/` — конвертеры на C# |
| **InfoSec Tools** | `crypto-tools-csharp/`, `infosec-means-csharp/`, `file-signature-csharp/` — инструменты ИБ |

---

## 🛠️ Технологический стек

| Категория | Технологии |
|-----------|------------|
| **Языки** | Python 3.12+, C# (.NET 6), SQL, Scilab |
| **GUI** | PyQt5, tkinter, WinForms, WPF, .NET MAUI |
| **Computer Vision** | OpenCV, face_recognition, dlib, Pillow |
| **Cryptography** | cryptography, hashlib, rsa, pycryptodome, Scapy |
| **Data & Math** | numpy, scipy, pandas, matplotlib, networkx |
| **Web Automation** | Selenium, BeautifulSoup, requests, lxml, python-whois |
| **Reporting** | reportlab, PyPDF2 |
| **Database** | SQLite |
| **Network** | socket, threading, Scapy, psutil, netifaces |

---

## 🚀 Быстрый старт

### 📋 Предварительные требования

- **Python 3.12+** ([скачать](https://www.python.org/downloads/))
- **pip >= 23.0**
- **Git** ([скачать](https://git-scm.com/))
- **Веб-камера** (для проектов компьютерного зрения)

### 📦 Установка зависимостей

```bash
# 🔹 Клонирование репозитория
git clone https://github.com/ACTLA/Internship-Portfolio.git
cd Internship-Portfolio

# 🔹 Основной проект (распознавание лиц)
cd computer-vision/face-recognition-system
pip install -r requirements.txt

# 🔹 Криптографический мессенджер
cd cryptography/protocols/secure-messenger-advanced/secure_messenger_trent
pip install -r requirements.txt

# 🔹 Веб-фиксация
cd web-automation/webpage-fixation/webpage_fixation
pip install -r requirements.txt

# 🔹 Глобальная установка всех зависимостей (опционально)
pip install -r requirements.txt  # в корне репозитория
```

### ▶️ Запуск проектов

```bash
# 🎭 Система распознавания лиц
cd computer-vision/face-recognition-system
python main.py

# 🔐 Криптографический мессенджер (3 терминала)
cd cryptography/protocols/secure-messenger-advanced/secure_messenger_trent
python trent.py    # Сервер ключей
python alice.py    # Клиент Alice
python bob.py      # Клиент Bob

# 📸 Веб-фиксация страницы
cd web-automation/webpage-fixation/webpage_fixation
python website_photorecording.py
```

---

## 📊 Статистика репозитория

| Метрика | Значение |
|---------|----------|
| **Файлов кода** | ~130+ |
| **Строк кода** | ~11,000+ |
| **Языков** | Python, C#, SQL, Scilab |
| **Период разработки** | 2022–2026 |
| **Статус** | 🟢 Активная разработка |

---

## 📬 Контакты

🌐 **GitHub:** [@ACTLA](https://github.com/ACTLA)  
🌐 **GitLab:** [tldaACTLA](https://gitlab.com/tldaACTLA)

---

## 📦 Репозитории

| Платформа | Ссылка |
|-----------|--------|
| **GitHub** | https://github.com/ACTLA/Internship-Portfolio.git |
| **GitLab** | https://gitlab.com/tldaACTLA/internship-portfolio.git |

---

*Разработано в рамках обучения по направлению «Информационная безопасность» и направлению «Фундаментальная информатика и информационные технологии», профиль «Интеллектуальный анализ данных»*