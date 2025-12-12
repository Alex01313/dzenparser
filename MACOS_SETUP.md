# macOS Setup Guide

This guide is specifically for macOS users setting up the Yandex Zen Article Parser.

## Prerequisites

### 1. Check Python Installation

Open Terminal and run:
```bash
python3 --version
```

You should see Python 3.8 or higher. If not, proceed to install Python.

### 2. Install Python (if needed)

**Option 1: Using Homebrew (Recommended)**
```bash
# Install Homebrew if not already installed
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Python
brew install python@3.11
```

**Option 2: Official Installer**
1. Visit https://www.python.org/downloads/macos/
2. Download Python 3.11 or later
3. Run the installer
4. Follow the installation wizard

### 3. Verify tkinter (GUI Library)

tkinter comes bundled with Python on macOS, but let's verify:
```bash
python3 -c "import tkinter; print('tkinter is available')"
```

If you see "tkinter is available", you're good to go!

## Installation

### Quick Setup (One Command)

```bash
cd /path/to/yandex-zen-parser
./run.sh
```

The `run.sh` script will:
- Check Python version
- Create a virtual environment (if needed)
- Install dependencies
- Launch the GUI

### Manual Setup

If you prefer to set up manually:

```bash
# 1. Navigate to the project directory
cd /path/to/yandex-zen-parser

# 2. Create virtual environment
python3 -m venv venv

# 3. Activate virtual environment
source venv/bin/activate

# 4. Upgrade pip
pip install --upgrade pip

# 5. Install dependencies
pip install -r requirements.txt

# 6. Run the application
python3 zen_parser_gui.py
```

## Running the Application

### Method 1: Using the Launcher Script
```bash
./run.sh
```

### Method 2: Direct Execution
```bash
# Activate virtual environment first
source venv/bin/activate

# Run the app
python3 zen_parser_gui.py

# When done, deactivate
deactivate
```

### Method 3: Make it executable
```bash
# Make the script executable (one-time setup)
chmod +x zen_parser_gui.py

# Run it
./zen_parser_gui.py
```

## macOS-Specific Features

### Keyboard Shortcuts

The application supports standard macOS keyboard shortcuts:

- **Cmd+V** - Paste URL in the input field
- **Cmd+C** - Copy selected text
- **Cmd+A** - Select all text in the display area
- **Cmd+Q** - Quit the application
- **Cmd+W** - Close the window

### Copy to Clipboard

The "Copy to Clipboard" button uses macOS's native clipboard, so the copied text works seamlessly with:
- TextEdit
- Pages
- Word
- Notes
- Any other macOS application

## Troubleshooting macOS Issues

### Issue 1: "Python is not installed as a framework"

**Symptom:**
```
RuntimeError: Python is not installed as a framework
```

**Solution:**
Use the Python from the official installer or Homebrew, not the system Python.

```bash
# Check which Python you're using
which python3

# Use Homebrew Python
brew install python@3.11

# Use that Python
/usr/local/bin/python3 zen_parser_gui.py
```

### Issue 2: "No module named 'tkinter'"

**Symptom:**
```
ModuleNotFoundError: No module named 'tkinter'
```

**Solution:**
Reinstall Python with tkinter support:

```bash
# Using Homebrew
brew reinstall python-tk@3.11
```

### Issue 3: Permission Denied

**Symptom:**
```
Permission denied: './zen_parser_gui.py'
```

**Solution:**
Make the file executable:

```bash
chmod +x zen_parser_gui.py
```

### Issue 4: SSL Certificate Error

**Symptom:**
```
SSL: CERTIFICATE_VERIFY_FAILED
```

**Solution:**
Install certificates:

```bash
# For Python installed via official installer
/Applications/Python\ 3.11/Install\ Certificates.command

# Or update certificates
pip install --upgrade certifi
```

### Issue 5: Application Doesn't Start

**Solution:**
Check logs and try verbose mode:

```bash
# Run with Python directly to see error messages
python3 -v zen_parser_gui.py
```

## macOS Security

### First Run - Gatekeeper

On first run, macOS Gatekeeper might show a security warning:

1. Click "Cancel" on the initial warning
2. Go to System Settings > Privacy & Security
3. Click "Open Anyway" next to the Python message
4. Confirm by clicking "Open"

### Allowing Network Access

If macOS asks to allow network access:
- Click "Allow" - the application needs internet to fetch articles

## Performance on macOS

### Expected Performance

- **Launch time:** 1-2 seconds
- **Parse time:** 2-5 seconds per article
- **Memory usage:** ~50-100 MB
- **CPU usage:** Minimal (spikes briefly during parsing)

### Optimizing Performance

For best performance on macOS:

1. **Close unnecessary applications** - Free up system resources
2. **Use a stable internet connection** - Wifi or ethernet
3. **Keep the application updated** - Pull latest changes regularly

## File Locations

### Virtual Environment
```
./venv/
```

### Application Data
The application doesn't store data, but creates:
- Virtual environment in `./venv/`
- Compiled Python files in `__pycache__/`

### Logs
No persistent logs are created. Errors appear in the GUI or Terminal.

## Uninstallation

To completely remove the application:

```bash
# 1. Navigate to the project directory
cd /path/to/yandex-zen-parser

# 2. Remove virtual environment
rm -rf venv/

# 3. Remove compiled files
rm -rf __pycache__/

# 4. Remove the entire directory (optional)
cd ..
rm -rf yandex-zen-parser/
```

## Creating an macOS App Bundle (Advanced)

If you want to create a double-clickable macOS app:

### Using py2app

```bash
# Install py2app
pip install py2app

# Create setup.py
cat > setup.py << 'EOF'
from setuptools import setup

APP = ['zen_parser_gui.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'packages': ['requests', 'bs4'],
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
EOF

# Build the app
python3 setup.py py2app

# The app will be in dist/zen_parser_gui.app
```

### Using PyInstaller

```bash
# Install PyInstaller
pip install pyinstaller

# Create the app
pyinstaller --onefile --windowed --name="Zen Parser" zen_parser_gui.py

# The app will be in dist/Zen Parser.app
```

## Integration with macOS

### Adding to Dock

1. Open the application
2. Right-click the icon in the Dock
3. Options > Keep in Dock

### Creating an Alias

```bash
# Create an alias in your bin directory
mkdir -p ~/bin
echo 'cd /path/to/yandex-zen-parser && ./run.sh' > ~/bin/zen-parser
chmod +x ~/bin/zen-parser

# Add to PATH (add to ~/.zshrc or ~/.bash_profile)
echo 'export PATH="$HOME/bin:$PATH"' >> ~/.zshrc

# Now you can run from anywhere
zen-parser
```

## Updates

To update the application:

```bash
cd /path/to/yandex-zen-parser

# Pull latest changes
git pull

# Update dependencies (if requirements.txt changed)
source venv/bin/activate
pip install -r requirements.txt --upgrade
```

## Support

For macOS-specific issues:
1. Check macOS version: `sw_vers`
2. Check Python version: `python3 --version`
3. Check if running on Apple Silicon: `uname -m` (arm64 = M1/M2/M3)
4. Report issues with these details

## macOS Version Compatibility

Tested and working on:
- macOS 14 (Sonoma)
- macOS 13 (Ventura)
- macOS 12 (Monterey)
- macOS 11 (Big Sur)
- macOS 10.15 (Catalina)

Should work on macOS 10.14 and later with Python 3.8+.

## Apple Silicon (M1/M2/M3) Notes

The application works natively on Apple Silicon Macs. No Rosetta 2 required.

```bash
# Verify you're running native ARM version
python3 -c "import platform; print(platform.machine())"
# Should output: arm64
```

---

**Happy Parsing!** 🚀
