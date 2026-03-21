# Engineering Portfolio

Репозиторий содержит коллекцию проектов по разработке программного обеспечения, криптографии, компьютерному зрению, сетевому программированию и алгоритмам.

---

## 📁 Структура репозитория

```
├── computer-vision/           # Компьютерное зрение
├── cryptography/              # Криптография и протоколы безопасности
├── encoding-compression/      # Кодирование и сжатие данных
├── network-programming/       # Сетевое программирование
├── web-automation/            # Веб-автоматизация
├── algorithms-data-structures/# Алгоритмы и структуры данных
├── numerical-methods/         # Численные методы
├── information-theory/        # Теория информации
├── docs/                      # Документация
└── Archive/                   # Архивные проекты (C#, Scilab, legacy)
```

---

## 🔍 Детальное описание проектов

### 1. Computer Vision (Компьютерное зрение)

#### **Face Recognition System** (`computer-vision/face-recognition-system/face_recognition_system/`)

Полнофункциональная система биометрической идентификации на основе распознавания лиц с модулем аудита безопасности.

**Архитектура:**
```
face_recognition_system/
├── main.py                 # Точка входа
├── requirements.txt        # Зависимости
├── config/                 # Конфигурационные файлы
├── core/                   # Ядро системы (распознавание, сравнение лиц)
├── gui/                    # Графический интерфейс
├── audit/                  # Модуль аудита и логирования событий
└── database/               # Базы данных пользователей
```

**Технологии:**
- `opencv-python` — обработка видеопотока
- `face_recognition` + `dlib` — распознавание лиц (CNN-модель)
- `PyQt5` — графический интерфейс
- `SQLite` — хранение пользователей и событий
- `cryptography` — шифрование чувствительных данных

**Функционал:**
- Распознавание лиц в реальном времени (30 FPS)
- Регистрация/удаление пользователей с генерацией биометрических отпечатков
- Система защиты от избыточных срабатываний (cooldown-механизм)
- Модуль аудита: логирование всех попыток распознавания, операций с БД, системных событий
- Экспорт отчётов в CSV для соответствия требованиям защиты персональных данных
- Трёхпанельный интерфейс: видеопоток, список пользователей, журнал событий

**Запуск:**
```bash
cd computer-vision/face-recognition-system/face_recognition_system
pip install -r requirements.txt
python main.py
```

---

### 2. Cryptography (Криптография)

#### **Modern Crypto** (`cryptography/modern-crypto/`)

| Проект | Путь | Описание |
|--------|------|----------|
| **RSA Block Cipher** | `rsa-block/rsa_block_cipher/` | RSA с блочным шифрованием, шифрование/дешифрование текстовых файлов |
| **RSA Basic** | `rsa-block/rsa_basic/` | Базовая реализация RSA (генерация ключей, шифрование) |
| **RSA Cryptanalysis** | `rsa-block/rsa_cryptanalysis/` | Криптоанализ RSA (факторизация, атаки) |
| **ElGamal** | `elgamal/elgamal_signature/` | ElGamal encryption + цифровая подпись |
| **GOST Signature** | `gost-signature/gost_r3410_94/` | ЭЦП по стандарту ГОСТ Р 34.10-94 |
| **Stream Ciphers** | `stream-ciphers/` | Гамма-шифр, LFSR, генераторы псевдослучайных чисел |

**Ключевые файлы:**
- `gost_signature_app.py` — приложение для подписи файлов по ГОСТ
- `gamma_cipher_encryption.py` — шифрование гаммой
- `elgamal_signature/` — подпись и проверка ElGamal

#### **Protocols** (`cryptography/protocols/`)

| Проект | Путь | Описание |
|--------|------|----------|
| **Secure Messenger (RSA)** | `secure-messenger-rsa/` | Мессенджер с RSA-шифрованием (клиент/сервер) |
| **Secure Messenger (Trent)** | `secure-messenger-advanced/secure_messenger_trent/` | Мессенджер с доверенной третьей стороной (Трент) |
| **SKID3 Protocol** | `skid3/` | Протокол аутентификации SKID3 |
| **Notary System** | `notary-system/` | Система «Нотариат» для цифровой подписи файлов |
| **Blakley Secret Sharing** | `blakley-secret-sharing/blakley_secret_sharing/` | Схема разделения секрета Блэкли |
| **Messenger Rabin MAUI** | `secure-messenger-advanced/messenger_rabin_maui/` | Мессенджер с обменом ключами Рабина (.NET MAUI) |

**Ключевые файлы:**
- `notary_service.py` — сервис цифровой подписи
- `trent.py`, `alice.py`, `bob.py` — сервер ключей и клиенты
- `skid3_client.py`, `skid3_server.py` — протокол SKID3

#### **Classical Ciphers** (`cryptography/classical-ciphers/`)

| Проект | Путь | Описание |
|--------|------|----------|
| **Affine Cipher** | `affine_cipher/` | Аффинный шифр (шифрование/дешифрование/криптоанализ) |
| **Permutation Cipher** | `permutation_cipher/` | Шифр перестановки |
| **Feistel Cipher** | `feistel-substitution/` | Сеть Фейстеля с S-блоками |

#### **Hash Functions** (`cryptography/hash-functions/`)

| Файл | Описание |
|------|----------|
| `crc_main.py` | CRC-32 хеширование |
| `crc_lab1.py` - `crc_lab6.py` | Различные реализации CRC |

#### **Cryptanalysis** (`cryptography/cryptanalysis/`)

| Файл | Описание |
|------|----------|
| `ferma_factorization.py` | Факторизация Ферма для взлома RSA |

---

### 3. Encoding & Compression (Кодирование и сжатие)

#### **Huffman** (`encoding-compression/huffman/`)

| Проект | Путь | Описание |
|--------|------|----------|
| **PyQt Advanced** | `pyqt-advanced/` | Хаффман с визуализацией дерева (NetworkX + Matplotlib) |
| **PyQt Basic** | `pyqt-basic/` | Базовая реализация с GUI |

**Функционал:**
- Построение дерева Хаффмана
- Визуализация структуры дерева
- Шифрование/дешифрование файлов
- Статистика сжатия

#### **Shannon-Fano** (`encoding-compression/shannon-fano/`)

| Проект | Путь | Описание |
|--------|------|----------|
| **Tkinter** | `tkinter/` | GUI на tkinter |
| **CLI** | `cli/` | Консольная версия |

#### **Arithmetic Coding** (`encoding-compression/arithmetic-coding/`)

| Проект | Путь | Описание |
|--------|------|----------|
| **PyQt** | `pyqt/` | Арифметическое кодирование с GUI |
| **Tkinter** | `tkinter/` | Версия на tkinter |

#### **LZ Algorithms** (`encoding-compression/lz-algorithms/`)

| Алгоритм | Путь | Описание |
|----------|------|----------|
| **LZ77** | `lz77-tkinter/` | Словарное сжатие LZ77 |
| **LZ78** | `lz78-pyqt/` | Словарное сжатие LZ78 |
| **LZW** | `lzw-cli/` | LZW компрессия |

#### **Error-Correcting Codes** (`encoding-compression/error-correcting/`)

| Код | Путь | Описание |
|-----|------|----------|
| **Hamming** | `hamming-pyqt/` | Код Хэмминга с исправлением одиночных ошибок |
| **Reed-Solomon** | `reed-solomon/` | Код Рида-Соломона (32 контрольных символа) |

**Ключевые файлы:**
- `hamming_pyqt.py` — GUI для кода Хэмминга
- `reed_solomon_pyqt.py` — кодирование/декодирование Рида-Соломона

#### **Encoding Converters** (`encoding-compression/encoding-converters/`)

| Проект | Путь | Описание |
|--------|------|----------|
| **PyQt** | `encoding_converter_pyqt/` | Конвертер кодировок с GUI |
| **CLI** | `encoding_converter_cli/` | Консольный конвертер |

---

### 4. Network Programming (Сетевое программирование)

#### **Socket Examples** (`network-programming/socket-examples/`)

| Файл | Описание |
|------|----------|
| `socket_client.py` | TCP-клиент |
| `socket_server.py` | TCP-сервер |
| `crypto_operations_gui.py` | GUI для криптографических операций |
| `socket_basic/` | Базовые примеры сокетов |

#### **Secure Chat** (`network-programming/secure-chat/`)

| Проект | Путь | Описание |
|--------|------|----------|
| **Fernet Chat** | `secure_chat_fernet/` | Защищённый чат с шифрованием Fernet |
| **C# Messenger** | `messenger_csharp_winforms/` | Мессенджер на C# WinForms |

**Ключевые файлы:**
- `client_alice.py`, `client_bob.py`, `server_trent.py` — клиенты и сервер

#### **MITM Simulations** (`network-programming/mitm-simulations/`)

| Проект | Путь | Описание |
|--------|------|----------|
| **ARP Spoofing** | `mitm_arp_spoofing/` | Симуляция ARP-spoofing атаки |
| **InfoSec Labs** | `infosec_labs/` | Лабораторные работы по безопасности |

**Файлы лабораторных:**
- `md5_hashing.py` — реализация MD5
- `digital_signature_md5.py` — ЭЦП на основе MD5
- `notary.py` — система нотариата
- `channel_interception.py` — перехват трафика

⚠️ **Предупреждение:** Код предназначен только для образовательных целей и тестирования в изолированной среде.

---

### 5. Web Automation (Веб-автоматизация)

#### **Web Saver** (`web-automation/web-saver/web_saver/`)

| Файл | Описание |
|------|----------|
| `main.py` | Сохранение веб-страниц с использованием Selenium |

**Функционал:**
- Автоматический скриншот веб-страницы
- Сохранение HTML-кода
- Генерация PDF-отчёта

#### **Webpage Fixation** (`web-automation/webpage-fixation/webpage_fixation/`)

| Файл | Описание |
|------|----------|
| `website_photorecording.py` | Фиксация веб-страниц с WHOIS/DNS данными |
| `package/` | Модули для сбора данных |

**Функционал:**
- Сбор WHOIS-информации о домене
- Выполнение и запись DNS-трассировки
- Создание полноразмерных скриншотов
- Объединение всех данных в единый PDF-документ
- Уникальный номер и временная метка для каждого отчёта

**Технологии:**
- `selenium` — автоматизация браузера
- `reportlab` — генерация PDF
- `beautifulsoup4` — парсинг HTML
- `python-whois` — WHOIS-запросы
- `Pillow` — обработка скриншотов

**Запуск:**
```bash
cd web-automation/webpage-fixation/webpage_fixation
pip install -r requirements.txt
python website_photorecording.py
```

---

### 6. Algorithms & Data Structures (Алгоритмы и структуры данных)

#### **Sorting** (`algorithms-data-structures/sorting/sorting_algorithms/`)

| Файл | Описание |
|------|----------|
| `poem_merge_sort.py` | Сортировка слиянием |
| `poem_quick_sort_hoare.py` | Быстрая сортировка (схема Хоара) |
| `poem_quick_sort_simple.py` | Быстрая сортировка (упрощённая) |

#### **Stacks & Queues** (`algorithms-data-structures/stacks-queues/`)

| Проект | Путь | Описание |
|--------|------|----------|
| **Calculator** | `stack_calculator/` | Калькулятор на основе стека |
| **Next Greater** | `stack_next_greater/` | Поиск следующего большего элемента |

#### **Graphs** (`algorithms-data-structures/graphs/graph_bus_path/`)

| Файл | Описание |
|------|----------|
| `bus_path.py` | Поиск оптимального маршрута на графе (алгоритм Дейкстры) |

---

### 7. Numerical Methods (Численные методы)

#### **Linear Algebra** (`numerical-methods/linear-algebra/linear_algebra_python/`)

| Файл | Описание |
|------|----------|
| `f1.py` | Операции с матрицами |
| `f2.py` | Решение систем линейных уравнений |
| `f3.py` | Вычисление собственных значений |
| `f4.py` | Метод наименьших квадратов |

#### **Interpolation** (`numerical-methods/interpolation/interpolation_python/`)

| Файл | Описание |
|------|----------|
| `four1.py` - `four8.py` | Интерполяционные полиномы, сплайны |

#### **Integration** (`numerical-methods/integration/integration_python/`)

| Файл | Описание |
|------|----------|
| `five1.py` | Метод трапеций |
| `five2.py` | Метод Симпсона |
| `ode_system.py` | Решение систем ОДУ |

#### **ODE Solving** (`numerical-methods/`)

| Файл | Описание |
|------|----------|
| `ode_solving.py` | Решение обыкновенных дифференциальных уравнений |

#### **Scilab Labs** (`numerical-methods/scilab-labs/scilab_labs/`)

9 лабораторных работ по численным методам в Scilab (Lab-1 — Lab-9).

---

### 8. Information Theory (Теория информации)

#### **Entropy Calculators** (`information-theory/entropy-calculators/`)

| Проект | Путь | Описание |
|--------|------|----------|
| **Python** | `python/urns_balls_python/` | Калькуляторы энтропии |
| **Python Advanced** | `python-advanced/` | Цепи Маркова с GUI |
| **C#** | `csharp/entropy_calculator_csharp/` | Калькулятор энтропии на C# |

---

## 📦 Archive (Архивные проекты)

В папке `Archive/` хранятся учебные работы, которые не являются основными для портфолио:

| Категория | Содержимое |
|-----------|------------|
| **C# Projects** | `desktop-apps/csharp-projects/` — проекты на .NET (WinForms, WPF, MAUI) |
| **Scilab Labs** | `numerical-methods/scilab-labs/` — лабораторные работы в Scilab |
| **Legacy Code** | `*/legacy/`, `*/tkinter/` — устаревшие версии на tkinter |
| **Classical Ciphers** | `cryptography/classical-ciphers/` — базовые шифры (аффинный, перестановки) |

---

## 🛠️ Технологический стек

| Категория | Технологии |
|-----------|------------|
| **Языки** | Python, SQL, C# (.NET 6) |
| **GUI** | PyQt5, tkinter, WinForms, WPF, MAUI |
| **Computer Vision** | OpenCV, face_recognition, dlib, Pillow |
| **Cryptography** | cryptography, hashlib, rsa, pycryptodome, Scapy |
| **Data & Math** | numpy, scipy, pandas, matplotlib, networkx |
| **Web Automation** | Selenium, BeautifulSoup, requests, lxml |
| **Reporting** | reportlab, PyPDF2 |
| **Database** | SQLite |
| **Network** | socket, threading, Scapy, psutil, netifaces |

---

## 📊 Статистика репозитория

| Метрика | Значение |
|---------|----------|
| **Всего проектов** | 50+ |
| **Файлов кода** | ~340 |
| **Строк кода** | ~15,000+ |
| **Период разработки** | 2022-2026 |

---

## 🚀 Быстрый старт

### Требования
- Python 3.12+
- pip >= 23.0
- Git

### Установка зависимостей
```bash
# Основной проект (распознавание лиц)
cd computer-vision/face-recognition-system/face_recognition_system
pip install -r requirements.txt

# Криптографический мессенджер
cd cryptography/protocols/secure-messenger-advanced/secure_messenger_trent
pip install -r requirements.txt

# Веб-фиксация
cd web-automation/webpage-fixation/webpage_fixation
pip install -r requirements.txt
```

### Запуск проектов
```bash
# Система распознавания лиц
cd computer-vision/face-recognition-system/face_recognition_system
python main.py

# Криптографический мессенджер
cd cryptography/protocols/secure-messenger-advanced/secure_messenger_trent
python trent.py    # Сервер ключей
python alice.py    # Клиент Alice
python bob.py      # Клиент Bob

# Веб-фиксация
cd web-automation/webpage-fixation/webpage_fixation
python website_photorecording.py
```

---

## 📬 Контакты

- **GitHub:** [Профиль GitHub](https://github.com/ACTLA)