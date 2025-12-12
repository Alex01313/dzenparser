# Quick Start Guide

Get up and running with Yandex Zen Article Parser in 3 minutes!

## ⚡ Super Quick Start (macOS)

```bash
# 1. Navigate to the project folder
cd /path/to/yandex-zen-parser

# 2. Run the launcher
./run.sh
```

That's it! The GUI will open automatically.

## 📝 First Use

### Step 1: Get a Yandex Zen URL
- Open your browser
- Go to https://zen.yandex.ru or https://dzen.ru
- Find any article
- Copy the URL (should look like: `https://zen.yandex.ru/media/...`)

### Step 2: Parse the Article
- Paste the URL in the "Article URL" field
- Click "Parse Article"
- Wait 2-5 seconds
- Extracted text appears below

### Step 3: Copy the Text
- Click "Copy to Clipboard"
- Paste anywhere with Cmd+V

## 🎯 Example Workflow

```
1. Launch: ./run.sh
2. Paste URL: https://zen.yandex.ru/media/...
3. Click: "Parse Article"
4. Click: "Copy to Clipboard"
5. Paste in your document (Cmd+V)
6. Done! ✅
```

## 🔧 One-Time Setup

Only needed the first time:

```bash
# Install Python (if not already installed)
brew install python@3.11

# Make scripts executable
chmod +x run.sh zen_parser_gui.py

# That's all!
```

## 📚 Common Commands

```bash
# Start the application
./run.sh

# Or directly
python3 zen_parser_gui.py

# Update dependencies (if needed)
source venv/bin/activate && pip install -r requirements.txt --upgrade
```

## ❓ Quick Troubleshooting

### "Permission denied"
```bash
chmod +x run.sh zen_parser_gui.py
```

### "Python not found"
```bash
brew install python@3.11
```

### "No text extracted"
- Check if URL is correct
- Try a different article
- Verify internet connection

## 📖 Learn More

- **Full documentation:** See [README.md](README.md)
- **macOS-specific help:** See [MACOS_SETUP.md](MACOS_SETUP.md)
- **Detailed examples:** See [EXAMPLES.md](EXAMPLES.md)

## 💡 Tips

- ✅ Use full URLs (not shortened links)
- ✅ Works with zen.yandex.ru, dzen.ru, zen.yandex.com
- ✅ Click "Clear" between articles to reset
- ✅ Status messages show progress and character count

## 🚀 Ready to Go!

```bash
./run.sh
```

Happy parsing! 🎉
