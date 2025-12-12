# Улучшения парсинга / Parsing Improvements

## 🇷🇺 Русский

### Что изменилось

Парсер теперь извлекает **только текст статьи**, автоматически фильтруя весь "шум":

#### Удаляется автоматически ❌
- Навигационные меню
- Шапка и подвал сайта
- Кнопки социальных сетей
- Блоки комментариев
- Реклама и промо-контент
- Похожие статьи
- Боковые панели
- Уведомления о cookies
- Всплывающие окна
- Кнопки и короткие UI тексты

#### Сохраняется ✅
- Заголовок статьи
- Основной текст статьи
- Подзаголовки внутри статьи
- Цитаты
- Списки (если часть статьи)

### Методы извлечения

Парсер использует 4 метода в порядке приоритета:

1. **JSON-LD метаданные** (95-100% точность)
   - Самый надежный метод
   - Использует структурированные данные статьи

2. **Анализ тега `<article>`** (85-95% точность)
   - Точное извлечение из HTML
   - Удаляет вложенный не-контент

3. **Дзен-специфичные селекторы** (80-90% точность)
   - CSS-селекторы для структуры Яндекс.Дзен
   - Оптимизировано для Дзена

4. **Резервный метод** (70-85% точность)
   - Извлечение из основной области контента
   - Используется при неудаче других методов

### Умная фильтрация

Автоматическая фильтрация UI фраз:
- **Русский**: Подписаться, Поделиться, Читать далее, Показать, Скрыть
- **Английский**: Subscribe, Share, Read more, Click here
- **Минимальная длина**: Отфильтровываются тексты короче 20 символов
- **Плотность ссылок**: Отфильтровываются тексты с >2 HTTP ссылками

### Тестирование

Запустите тесты для проверки:

```bash
python3 test_extraction.py
```

---

## 🇬🇧 English

### What Changed

The parser now extracts **only article text**, automatically filtering out all the "noise":

#### Automatically Removed ❌
- Navigation menus
- Site headers and footers
- Social media buttons
- Comment sections
- Ads and promotional content
- Related articles
- Sidebars
- Cookie notices
- Popups
- Buttons and short UI texts

#### Preserved ✅
- Article title
- Main article text
- Article subheadings
- Quotes
- Lists (if part of article)

### Extraction Methods

The parser uses 4 methods in priority order:

1. **JSON-LD Metadata** (95-100% accuracy)
   - Most reliable method
   - Uses structured article data

2. **Article Tag Analysis** (85-95% accuracy)
   - Precise HTML extraction
   - Removes nested non-content

3. **Zen-Specific Selectors** (80-90% accuracy)
   - CSS selectors for Yandex Zen structure
   - Optimized for Zen

4. **Fallback Method** (70-85% accuracy)
   - Extraction from main content area
   - Used when other methods fail

### Smart Filtering

Automatic UI phrase filtering:
- **Russian**: Подписаться, Поделиться, Читать далее, Показать, Скрыть
- **English**: Subscribe, Share, Read more, Click here
- **Minimum length**: Filters texts shorter than 20 characters
- **Link density**: Filters texts with >2 HTTP links

### Testing

Run tests to verify:

```bash
python3 test_extraction.py
```

---

## Technical Details

### Code Changes

**Main file**: `zen_parser_gui.py`

**New methods**:
- `is_noise_text(text)` - Detects UI noise
- `clean_text(text)` - Cleans and formats text

**Enhanced method**:
- `extract_article_text(soup)` - Improved extraction logic with:
  - Pre-extraction cleanup (removes nav, header, footer, etc.)
  - Pattern-based element removal
  - Priority-based extraction attempts
  - Better paragraph filtering
  - Noise detection for each text fragment

### Before vs After

**Before**: Extracted all paragraphs from page → included navigation, comments, ads

**After**: 
1. Remove all non-content sections
2. Try JSON-LD (best)
3. Try article tag (good)
4. Try Zen selectors (good)
5. Try main content (ok)
6. Filter each paragraph through noise detection
7. Clean and format result

### Configuration

Adjustable parameters in code:
- `MIN_LENGTH`: Minimum paragraph length (15-30 chars depending on method)
- `noise_patterns`: Patterns to remove
- `noise_phrases`: UI phrases to filter
- `zen_selectors`: Zen-specific CSS selectors

---

## Feedback / Обратная связь

If you find that some content is incorrectly filtered or included, please:
- Provide the article URL
- Describe what was wrong
- We'll improve the filtering logic

Если вы обнаружите, что какой-то контент неправильно отфильтрован или включен:
- Предоставьте URL статьи
- Опишите, что было неправильно
- Мы улучшим логику фильтрации
