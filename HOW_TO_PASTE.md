# How to Paste URLs / Как вставить URL

## 🎯 Quick Answer / Быстрый ответ

**Problem:** Can't paste URL with Cmd+V or right-click?  
**Solution:** ✅ **FIXED!** Now it works!

**Проблема:** Не можете вставить URL с помощью Cmd+V или правой кнопки?  
**Решение:** ✅ **ИСПРАВЛЕНО!** Теперь работает!

---

## 🚀 How to Paste / Как вставить

### Method 1: Cmd+V (macOS) ⭐ RECOMMENDED

```
Step 1: Copy URL
   Open browser → Find article → Copy URL (Cmd+C)
   Example: https://dzen.ru/a/aTsmd_bGr2aapkGO

Step 2: Open Parser
   ./run.sh

Step 3: Paste
   Click in "Article URL" field
   Press: Cmd+V
   Result: ✅ URL is pasted!
```

### Метод 1: Cmd+V (macOS) ⭐ РЕКОМЕНДУЕТСЯ

```
Шаг 1: Скопируйте URL
   Откройте браузер → Найдите статью → Скопируйте URL (Cmd+C)
   Пример: https://dzen.ru/a/aTsmd_bGr2aapkGO

Шаг 2: Откройте парсер
   ./run.sh

Шаг 3: Вставьте
   Кликните в поле "Article URL"
   Нажмите: Cmd+V
   Результат: ✅ URL вставлен!
```

---

### Method 2: Right-Click Menu / Контекстное меню

```
Step 1: Copy URL (Cmd+C)

Step 2: Open Parser
   ./run.sh

Step 3: Right-Click in URL field
   A menu will appear with options:
   - Cut
   - Copy
   - Paste    ← Click here!
   - Select All

Step 4: Click "Paste"
   Result: ✅ URL is pasted!
```

```
Шаг 1: Скопируйте URL (Cmd+C)

Шаг 2: Откройте парсер
   ./run.sh

Шаг 3: Кликните правой кнопкой в поле URL
   Появится меню с опциями:
   - Cut (Вырезать)
   - Copy (Копировать)
   - Paste (Вставить)    ← Кликните сюда!
   - Select All (Выбрать всё)

Шаг 4: Нажмите "Paste"
   Результат: ✅ URL вставлен!
```

---

### Method 3: Ctrl+V (Alternative) / Альтернатива

Even on macOS, Ctrl+V also works now!

```
Click in URL field
Press: Ctrl+V (instead of Cmd+V)
Result: ✅ Works!
```

Даже на macOS, Ctrl+V тоже работает!

```
Кликните в поле URL
Нажмите: Ctrl+V (вместо Cmd+V)
Результат: ✅ Работает!
```

---

## 🎨 Visual Guide / Визуальная инструкция

### Step-by-Step / Пошагово:

```
1. [Browser] https://dzen.ru/a/test123
              ↓
           [Cmd+C]
              ↓
           [Copied!]

2. [Terminal] ./run.sh
              ↓
           [GUI Opens]

3. [GUI] Article URL: [_____________]
              ↓
         [Click here]
              ↓
         [Cmd+V or Right-Click]
              ↓
    Article URL: [https://dzen.ru/a/test123]
              ↓
           [Success! ✅]
```

---

## 🔑 All Keyboard Shortcuts / Все горячие клавиши

### macOS:

| Key | Action |
|-----|--------|
| `⌘ + V` | Paste URL ⭐ |
| `⌘ + C` | Copy URL |
| `⌘ + X` | Cut URL |
| `⌘ + A` | Select All |

### Windows/Linux:

| Key | Action |
|-----|--------|
| `Ctrl + V` | Paste URL ⭐ |
| `Ctrl + C` | Copy URL |
| `Ctrl + X` | Cut URL |
| `Ctrl + A` | Select All |

---

## ❓ Troubleshooting / Решение проблем

### Still can't paste? / Всё ещё не можете вставить?

#### Try this / Попробуйте это:

**Option 1: Check Clipboard**
```
Test if URL is in clipboard:
- Try pasting in TextEdit/Notepad first
- If that works, clipboard is OK
```

**Option 2: Restart App**
```
Close parser → ./run.sh → Try again
```

**Option 3: Type Manually**
```
If all else fails, just type the URL:
Click in field → Type: https://dzen.ru/a/...
```

**Опция 1: Проверьте буфер обмена**
```
Проверьте, есть ли URL в буфере обмена:
- Попробуйте вставить в TextEdit/Блокнот сначала
- Если работает, буфер в порядке
```

**Опция 2: Перезапустите приложение**
```
Закройте парсер → ./run.sh → Попробуйте снова
```

**Опция 3: Введите вручную**
```
Если ничего не помогает, просто введите URL:
Кликните в поле → Введите: https://dzen.ru/a/...
```

---

## 📱 Quick Tips / Быстрые советы

### English:

1. **Cmd+V is fastest** - Use it as default method
2. **Right-click always works** - Good backup option
3. **Both Cmd and Ctrl work** - Use what you prefer
4. **Click field first** - Make sure field is focused
5. **Context menu shows on right-click** - Easy access

### Русский:

1. **Cmd+V самый быстрый** - Используйте его по умолчанию
2. **Правая кнопка всегда работает** - Хороший запасной вариант
3. **Работают и Cmd, и Ctrl** - Используйте что предпочитаете
4. **Сначала кликните в поле** - Убедитесь что поле активно
5. **Контекстное меню по правой кнопке** - Легкий доступ

---

## 🎓 Common Mistakes / Распространенные ошибки

### Mistake 1: Field not focused / Поле не активно

**Wrong:**
```
Press Cmd+V without clicking in field
→ Nothing happens ❌
```

**Correct:**
```
Click in URL field FIRST
Then press Cmd+V
→ Works! ✅
```

### Mistake 2: Wrong shortcut / Неправильное сочетание

**Wrong on macOS:**
```
Press Ctrl+V (old habit from Windows)
Wait... actually this works too! ✅
```

**Note:** Both Cmd+V and Ctrl+V work on macOS now!

### Mistake 3: Nothing in clipboard / Нет ничего в буфере

**Problem:**
```
Press Cmd+V → Nothing happens
```

**Solution:**
```
Go back to browser
Select URL
Copy again (Cmd+C)
Try paste again
```

---

## 📊 What Changed? / Что изменилось?

### Before (v1.1.0):

```
❌ Cmd+V didn't work
❌ Right-click had no menu
❌ Had to type URLs manually
😡 Frustrating experience
```

### After (v1.1.1):

```
✅ Cmd+V works perfectly
✅ Right-click shows menu
✅ Ctrl+V also works
✅ Standard shortcuts work
😊 Smooth experience
```

---

## 🔗 More Info / Дополнительная информация

For complete keyboard shortcuts list:
→ See [KEYBOARD_SHORTCUTS.md](KEYBOARD_SHORTCUTS.md)

For technical details about the fix:
→ See [PASTE_FIX.md](PASTE_FIX.md)

For quick reference:
→ See [QUICK_REFERENCE.md](QUICK_REFERENCE.md)

---

## ✅ Summary / Резюме

### The Bottom Line / Вывод:

**English:**
Paste now works! Use Cmd+V (fastest) or right-click menu (easiest). Both methods work perfectly.

**Русский:**
Вставка теперь работает! Используйте Cmd+V (быстрее всего) или контекстное меню (проще всего). Оба метода работают отлично.

---

**Fixed in:** v1.1.1  
**Date:** 2024-12-12  
**Status:** ✅ Working perfectly!
