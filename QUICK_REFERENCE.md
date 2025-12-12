# Quick Reference Card / Краткая справка

## 🚀 Start the Parser / Запуск парсера

```bash
./run.sh
```

## 📋 Supported URLs / Поддерживаемые URL

| Format / Формат | Example / Пример | Status |
|----------------|------------------|--------|
| **Short / Короткий** | `https://dzen.ru/a/aTsmd_bGr2aapkGO` | ✅ |
| **Long / Длинный** | `https://zen.yandex.ru/media/id/123/title` | ✅ |
| **Alt Domain 1** | `https://dzen.ru/media/...` | ✅ |
| **Alt Domain 2** | `https://zen.yandex.com/...` | ✅ |
| **HTTP** | `http://dzen.ru/a/test` | ✅ |

## 🎯 Quick Usage / Быстрое использование

```
1. Copy URL   → https://dzen.ru/a/[id]
2. Launch     → ./run.sh
3. Paste URL  → Article URL field
4. Click      → "Parse Article"
5. Copy       → "Copy to Clipboard"
```

## 📁 Project Files / Файлы проекта

| File | Purpose |
|------|---------|
| `zen_parser_gui.py` | Main application |
| `run.sh` | Launcher script |
| `requirements.txt` | Dependencies |
| `test_extraction.py` | Extraction tests |
| `test_url_formats.py` | URL format tests |

## 📖 Documentation / Документация

| File | Description |
|------|-------------|
| `README.md` | Main docs (EN) |
| `README_RU.md` | Main docs (RU) |
| `QUICKSTART.md` | Quick start guide |
| `URL_FORMATS.md` | All URL formats |
| `EXAMPLES.md` | Usage examples |
| `PARSING_DETAILS.md` | Parser internals |

## 🧪 Testing / Тестирование

```bash
# Test extraction logic
python3 test_extraction.py

# Test URL formats
python3 test_url_formats.py

# Test GUI (requires display)
python3 test_parser.py
```

## ⚙️ Installation / Установка

```bash
# One-time setup
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Run
./run.sh
```

## ✨ Features / Функции

- ✅ Extracts article text only / Только текст статьи
- ✅ Filters noise (ads, nav, etc.) / Фильтрует шум
- ✅ All URL formats / Все форматы URL
- ✅ Copy to clipboard / Копирование в буфер
- ✅ Error handling / Обработка ошибок
- ✅ macOS compatible / Совместимость с macOS

## 🔑 Keyboard Shortcuts (macOS)

- `Cmd+V` - Paste URL
- `Cmd+C` - Copy text
- `Cmd+A` - Select all
- `Cmd+Q` - Quit app

## 💡 Tips / Советы

1. Use short URLs for convenience / Используйте короткие ссылки для удобства
2. Check status messages / Проверяйте статусные сообщения
3. Works with all domains / Работает со всеми доменами
4. No manual URL editing needed / Не нужно редактировать URL вручную

## ❓ Quick Troubleshooting / Быстрое решение проблем

| Problem | Solution |
|---------|----------|
| "Permission denied" | `chmod +x run.sh zen_parser_gui.py` |
| "Python not found" | `brew install python@3.11` |
| "Invalid URL" | Check protocol (http/https) |
| "No text extracted" | Try different article |

## 📞 Help / Помощь

- 📚 Full docs: See [README.md](README.md)
- 🌐 URL help: See [URL_FORMATS.md](URL_FORMATS.md)
- 💻 Examples: See [EXAMPLES.md](EXAMPLES.md)
- 🇷🇺 Русский: See [README_RU.md](README_RU.md)

---

**Version:** 1.1.0 | **License:** MIT | **Platform:** macOS (cross-platform compatible)
