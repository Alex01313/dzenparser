# Selenium Setup Guide / Руководство по установке Selenium

## 🚀 Зачем нужен Selenium? / Why Selenium?

Некоторые статьи Dzen используют JavaScript для загрузки контента. Обычный парсер (requests) не может выполнить JavaScript, поэтому страница остается пустой.

**Selenium решает эту проблему!** Он запускает реальный браузер, который выполняет весь JavaScript.

---

## ✅ Быстрая установка / Quick Installation

### macOS

```bash
# 1. Установите Python зависимости
pip install selenium

# 2. Установите ChromeDriver через Homebrew
brew install chromedriver

# 3. Разрешите выполнение ChromeDriver
xattr -d com.apple.quarantine $(which chromedriver)

# Готово! ✅
```

### Альтернатива (webdriver-manager)

```bash
# Автоматическая установка драйвера
pip install selenium webdriver-manager
```

Тогда в коде использовать:
```python
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
```

---

## 📋 Полная инструкция / Detailed Instructions

### Шаг 1: Установите Selenium

```bash
cd /path/to/yandex-zen-parser
source venv/bin/activate
pip install selenium
```

### Шаг 2: Установите Chrome (если нет)

Скачайте с: https://www.google.com/chrome/

### Шаг 3: Установите ChromeDriver

#### Способ 1: Homebrew (рекомендуется для macOS)

```bash
brew install chromedriver
```

#### Способ 2: Вручную

1. Узнайте версию Chrome:
   - Откройте Chrome
   - Перейдите в `chrome://version/`
   - Запомните версию (например, 120.0.6099.109)

2. Скачайте соответствующий ChromeDriver:
   - https://chromedriver.chromium.org/downloads
   - Или https://googlechromelabs.github.io/chrome-for-testing/

3. Распакуйте и переместите:
   ```bash
   unzip chromedriver_mac64.zip
   sudo mv chromedriver /usr/local/bin/
   chmod +x /usr/local/bin/chromedriver
   ```

4. Разрешите выполнение (macOS):
   ```bash
   xattr -d com.apple.quarantine /usr/local/bin/chromedriver
   ```

### Шаг 4: Проверьте установку

```bash
chromedriver --version
```

Должно показать что-то вроде:
```
ChromeDriver 120.0.6099.109
```

---

## 🧪 Тестирование / Testing

### Тест 1: Проверка ChromeDriver

```bash
python3 -c "from selenium import webdriver; driver = webdriver.Chrome(); print('OK'); driver.quit()"
```

Если выдает `OK` - все работает! ✅

### Тест 2: Проверка парсинга

```bash
cd /home/engine/project
python3 zen_parser_selenium.py
```

### Тест 3: Проверка в GUI

```bash
./run.sh
```

1. Вставьте URL
2. ✅ Поставьте галочку "Use JavaScript Rendering"
3. Нажмите "Parse Article"

---

## 🎯 Как использовать / How to Use

### В GUI приложении:

1. **Запустите парсер:**
   ```bash
   ./run.sh
   ```

2. **Вставьте URL статьи:**
   ```
   https://dzen.ru/a/aTsmd_bGr2aapkGO
   ```

3. **Включите Selenium:**
   - ✅ Поставьте галочку: "🚀 Use JavaScript Rendering (Selenium)"

4. **Нажмите "Parse Article"**

5. **Готово!** Текст должен извлечься ✅

### Когда использовать Selenium:

✅ **Используйте** если:
- Статья открывается в браузере, но парсер выдает ошибку
- Получаете "Authentication required" но статья публична
- Страница маленькая (< 5KB)
- Контент загружается через JavaScript

❌ **Не используйте** если:
- Обычный парсинг работает (быстрее)
- Статья действительно требует авторизацию

---

## ⚙️ Настройка / Configuration

### requirements.txt

Убедитесь, что в `requirements.txt` есть:

```
selenium>=4.15.0
```

### Установка зависимостей:

```bash
pip install -r requirements.txt
```

---

## ❓ Решение проблем / Troubleshooting

### Проблема 1: "chromedriver not found"

**Решение:**
```bash
# macOS
brew install chromedriver

# Или укажите путь явно
export PATH="/usr/local/bin:$PATH"
```

### Проблема 2: "ChromeDriver can't be opened"

**Решение (macOS):**
```bash
xattr -d com.apple.quarantine $(which chromedriver)
```

Или:
```bash
# Откройте System Settings > Privacy & Security
# Нажмите "Open Anyway" для chromedriver
```

### Проблема 3: "Chrome version mismatch"

**Решение:**
```bash
# Обновите Chrome до последней версии
# Обновите ChromeDriver
brew upgrade chromedriver
```

### Проблема 4: "Session not created"

**Причины:**
- Версии Chrome и ChromeDriver не совпадают
- Chrome не установлен

**Решение:**
```bash
# Проверьте версию Chrome
chrome --version

# Проверьте версию ChromeDriver
chromedriver --version

# Они должны совпадать (первые две цифры)
```

### Проблема 5: Медленная работа

**Решение:**
- Это нормально! Selenium медленнее обычного парсинга
- Ожидайте 10-15 секунд вместо 2-5

**Оптимизация:**
```python
# В коде уже включено:
# - Headless mode (без окна)
# - Отключены изображения
# - Минимальные ожидания
```

---

## 🔍 Альтернативы / Alternatives

### Вариант 1: webdriver-manager (автоматический)

```bash
pip install webdriver-manager
```

Автоматически скачивает нужную версию ChromeDriver.

### Вариант 2: Другие браузеры

#### Firefox:

```bash
brew install geckodriver
pip install selenium
```

```python
from selenium import webdriver
driver = webdriver.Firefox()
```

#### Safari:

```bash
# Safari WebDriver встроен в macOS
safaridriver --enable
```

```python
from selenium import webdriver
driver = webdriver.Safari()
```

---

## 📊 Сравнение методов / Comparison

| Метод | Скорость | JavaScript | Требования |
|-------|----------|------------|------------|
| Requests | ⚡⚡⚡ Быстро | ❌ Нет | requests, bs4 |
| Selenium | 🐌 Медленно | ✅ Да | + ChromeDriver |

**Рекомендация:**
- Сначала пробуйте обычный парсинг
- Если не работает → включайте Selenium

---

## 🎓 Примеры / Examples

### Пример 1: Обычная статья

```
URL: https://zen.yandex.ru/media/...
Selenium: ❌ Не нужен
Результат: ✅ Работает без Selenium
```

### Пример 2: JavaScript статья

```
URL: https://dzen.ru/a/aTsmd_bGr2aapkGO
Обычный парсинг: ❌ Редирект на SSO
Selenium: ✅ Работает!
Результат: ✅ Текст извлечен
```

### Пример 3: Защищенная статья

```
URL: Требует вход в аккаунт
Selenium: ❌ Не поможет
Результат: ❌ Нужна авторизация
```

---

## 📝 Чеклист установки / Installation Checklist

- [ ] Python 3.8+ установлен
- [ ] pip работает
- [ ] selenium установлен (`pip install selenium`)
- [ ] Chrome установлен
- [ ] ChromeDriver установлен
- [ ] ChromeDriver в PATH
- [ ] ChromeDriver разрешен в Security (macOS)
- [ ] Тест запускается: `chromedriver --version`
- [ ] Selenium работает: `python3 zen_parser_selenium.py`
- [ ] GUI показывает чекбокс "Use JavaScript Rendering"

---

## 💡 Советы / Tips

### Для быстрой работы:

1. **Используйте кэш:** Сохраняйте статьи локально
2. **Batch processing:** Парсите несколько статей подряд
3. **Headless mode:** Уже включен (без GUI браузера)
4. **Отключите изображения:** Уже сделано

### Для надежности:

1. **Обновляйте ChromeDriver:** Раз в месяц
2. **Проверяйте версии:** Chrome и ChromeDriver должны совпадать
3. **Обрабатывайте ошибки:** Парсер уже это делает
4. **Используйте таймауты:** Уже настроено (30 сек)

---

## 🔗 Полезные ссылки / Useful Links

**Официальная документация:**
- Selenium: https://www.selenium.dev/documentation/
- ChromeDriver: https://chromedriver.chromium.org/

**Скачать:**
- Chrome: https://www.google.com/chrome/
- ChromeDriver: https://googlechromelabs.github.io/chrome-for-testing/
- Homebrew: https://brew.sh/

**Помощь:**
- Selenium Python: https://selenium-python.readthedocs.io/
- Stack Overflow: https://stackoverflow.com/questions/tagged/selenium

---

## ✅ Готово! / Ready!

После установки:

1. Запустите парсер:
   ```bash
   ./run.sh
   ```

2. Включите чекбокс:
   ```
   ✅ Use JavaScript Rendering (Selenium)
   ```

3. Парсите статьи с JavaScript! 🚀

---

**Дата:** 2024-12-12  
**Версия:** 1.1.2  
**Статус:** Selenium поддержка добавлена ✅
