# Supported URL Formats / Поддерживаемые форматы URL

## 🇬🇧 English

### All Supported Formats

The Yandex Zen Article Parser supports **all URL formats** used by Yandex Zen and Dzen:

#### ✅ Short Format (Current / Recommended)

The new short URL format used by Dzen:

```
https://dzen.ru/a/aTsmd_bGr2aapkGO
https://dzen.ru/a/ZAbCdEfGhIjKlMnO
https://dzen.ru/a/[article-id]
```

**Features:**
- ✅ Shorter, easier to share
- ✅ Current standard on dzen.ru
- ✅ Works perfectly with the parser
- ✅ Example: `https://dzen.ru/a/aTsmd_bGr2aapkGO`

#### ✅ Long Format (Legacy)

The traditional format with full path:

```
https://zen.yandex.ru/media/id/5f6c9e8f/article-title-123
https://zen.yandex.ru/media/channelname/article-title
https://dzen.ru/media/example/article-name
```

**Features:**
- ✅ Still widely used
- ✅ Contains readable article title
- ✅ Full compatibility

#### ✅ Alternative Domains

All three domains are supported:

```
https://zen.yandex.ru/...   (Original Russian domain)
https://dzen.ru/...          (New primary domain)
https://zen.yandex.com/...   (International version)
```

#### ✅ HTTP and HTTPS

Both protocols work:

```
https://dzen.ru/a/test123  ✅ (Recommended)
http://dzen.ru/a/test123   ✅ (Also works)
```

### Testing

You can test URL validation with:

```bash
python3 test_url_formats.py
```

---

## 🇷🇺 Русский

### Все поддерживаемые форматы

Парсер статей Яндекс.Дзен поддерживает **все форматы URL**, используемые Яндекс.Дзен и Дзен:

#### ✅ Короткий формат (текущий / рекомендуется)

Новый короткий формат URL, используемый Дзеном:

```
https://dzen.ru/a/aTsmd_bGr2aapkGO
https://dzen.ru/a/ZAbCdEfGhIjKlMnO
https://dzen.ru/a/[идентификатор-статьи]
```

**Особенности:**
- ✅ Короче, удобнее делиться
- ✅ Текущий стандарт на dzen.ru
- ✅ Отлично работает с парсером
- ✅ Пример: `https://dzen.ru/a/aTsmd_bGr2aapkGO`

#### ✅ Длинный формат (устаревший)

Традиционный формат с полным путем:

```
https://zen.yandex.ru/media/id/5f6c9e8f/название-статьи-123
https://zen.yandex.ru/media/имяканала/название-статьи
https://dzen.ru/media/пример/название-статьи
```

**Особенности:**
- ✅ Все еще широко используется
- ✅ Содержит читаемое название статьи
- ✅ Полная совместимость

#### ✅ Альтернативные домены

Поддерживаются все три домена:

```
https://zen.yandex.ru/...   (Оригинальный российский домен)
https://dzen.ru/...          (Новый основной домен)
https://zen.yandex.com/...   (Международная версия)
```

#### ✅ HTTP и HTTPS

Работают оба протокола:

```
https://dzen.ru/a/test123  ✅ (Рекомендуется)
http://dzen.ru/a/test123   ✅ (Тоже работает)
```

### Тестирование

Вы можете протестировать валидацию URL с помощью:

```bash
python3 test_url_formats.py
```

---

## URL Format Examples / Примеры форматов URL

### Valid URLs / Правильные URL ✅

```
✅ https://dzen.ru/a/aTsmd_bGr2aapkGO
✅ https://dzen.ru/a/YbXz1234567890
✅ https://zen.yandex.ru/media/id/5f6c9e8f7d0a2a6b1c8f9a0b/title-123
✅ https://zen.yandex.ru/media/channelname/article-title
✅ https://dzen.ru/media/example/article-name
✅ https://zen.yandex.com/media/id/123/article-456
✅ http://dzen.ru/a/test123
✅ https://dzen.ru/id/5f6c9e8f7d0a2a6b1c8f9a0b
```

### Invalid URLs / Неправильные URL ❌

```
❌ dzen.ru/a/test                    (Missing protocol)
❌ https://google.com/article        (Wrong domain)
❌ www.dzen.ru/a/test                (Missing protocol)
❌ ftp://dzen.ru/a/test              (Wrong protocol - use http/https)
```

---

## Technical Details / Технические детали

### URL Validation Logic

The parser validates URLs by checking:

1. **Protocol**: Must have `http://` or `https://`
2. **Domain**: Must contain one of:
   - `zen.yandex.ru`
   - `dzen.ru`
   - `zen.yandex.com`
3. **Path**: Any path is accepted (no restrictions)

### Code Reference

Validation is implemented in `zen_parser_gui.py`:

```python
def validate_url(self, url):
    parsed = urlparse(url)
    if not parsed.scheme:
        return False, "URL must include http:// or https://"
    
    zen_domains = ['zen.yandex.ru', 'dzen.ru', 'zen.yandex.com']
    if not any(domain in parsed.netloc for domain in zen_domains):
        return False, "URL must be from Yandex Zen"
    
    return True, "Valid URL"
```

---

## Real-World Examples / Примеры из жизни

### Example 1: Short URL / Короткая ссылка

```
URL: https://dzen.ru/a/aTsmd_bGr2aapkGO
Type: Short format
Domain: dzen.ru
Path: /a/aTsmd_bGr2aapkGO
Status: ✅ Supported
```

### Example 2: Long URL with Title / Длинная ссылка с названием

```
URL: https://zen.yandex.ru/media/tech/best-phones-2024-review
Type: Long format
Domain: zen.yandex.ru
Path: /media/tech/best-phones-2024-review
Status: ✅ Supported
```

### Example 3: Alternative Domain / Альтернативный домен

```
URL: https://zen.yandex.com/media/id/123/article
Type: Long format
Domain: zen.yandex.com
Path: /media/id/123/article
Status: ✅ Supported
```

---

## FAQ

### Q: Do I need to use a specific format?
**A:** No! All formats work equally well. Use whatever URL you get from Dzen.

### Q: Does the short format work?
**A:** Yes! `https://dzen.ru/a/...` format is fully supported.

### Q: Can I use HTTP instead of HTTPS?
**A:** Yes, but HTTPS is recommended for security.

### Q: What if my URL doesn't work?
**A:** Make sure it:
1. Includes `http://` or `https://`
2. Is from `zen.yandex.ru`, `dzen.ru`, or `zen.yandex.com`
3. Is a valid article link (not just the homepage)

---

### В: Нужно ли использовать определенный формат?
**О:** Нет! Все форматы работают одинаково хорошо. Используйте любую ссылку из Дзена.

### В: Работает ли короткий формат?
**О:** Да! Формат `https://dzen.ru/a/...` полностью поддерживается.

### В: Могу ли я использовать HTTP вместо HTTPS?
**О:** Да, но HTTPS рекомендуется для безопасности.

### В: Что делать, если моя ссылка не работает?
**О:** Убедитесь, что она:
1. Содержит `http://` или `https://`
2. С домена `zen.yandex.ru`, `dzen.ru` или `zen.yandex.com`
3. Это ссылка на статью (не просто главная страница)

---

## Summary / Резюме

**All Yandex Zen / Dzen URL formats are supported!** ✅

Whether you have:
- Short URLs (`dzen.ru/a/...`)
- Long URLs (`zen.yandex.ru/media/...`)
- Any of the three domains

The parser will work! Just paste the URL and click "Parse Article".

**Все форматы URL Яндекс.Дзен / Дзен поддерживаются!** ✅

Независимо от того, есть ли у вас:
- Короткие ссылки (`dzen.ru/a/...`)
- Длинные ссылки (`zen.yandex.ru/media/...`)
- Любой из трех доменов

Парсер будет работать! Просто вставьте URL и нажмите "Parse Article".
