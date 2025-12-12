# Yandex Zen Article Parser

> 🇷🇺 [Русская версия документации](README_RU.md)

A Python GUI application for extracting article text from Yandex Zen (Дзен) articles. This application provides a user-friendly interface to parse and extract **clean article text only**, filtering out navigation, ads, comments, and other page elements. Fully compatible with macOS.

## Features

- **User-Friendly GUI**: Clean and intuitive interface built with tkinter
- **URL Validation**: Validates Yandex Zen URLs before parsing
- **Article Extraction**: Extracts main article text from Yandex Zen pages
- **Copy to Clipboard**: Easy one-click copying of extracted text
- **Error Handling**: Comprehensive error handling for network issues, invalid URLs, and parsing errors
- **macOS Compatible**: Fully tested and compatible with macOS

## Requirements

- Python 3.8 or higher
- Internet connection for fetching articles

## Installation

### 1. Clone or download this repository

```bash
git clone <repository-url>
cd <repository-directory>
```

### 2. Create a virtual environment (recommended)

```bash
python3 -m venv venv
source venv/bin/activate  # On macOS/Linux
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## Usage

### Running the Application

```bash
python3 zen_parser_gui.py
```

Or make it executable:

```bash
chmod +x zen_parser_gui.py
./zen_parser_gui.py
```

### Using the Application

1. **Launch the application** by running the command above
2. **Enter a Yandex Zen article URL** in the input field
   - Supported domains: `zen.yandex.ru`, `dzen.ru`, `zen.yandex.com`
3. **Click "Parse Article"** to extract the text
4. **View the extracted text** in the main text area
5. **Click "Copy to Clipboard"** to copy the text for use elsewhere
6. **Click "Clear"** to reset the interface

### Example URLs

The parser supports all Yandex Zen / Dzen URL formats:

**Short format (new):**
- `https://dzen.ru/a/aTsmd_bGr2aapkGO`
- `https://dzen.ru/a/[article-id]`

**Long format (legacy):**
- `https://zen.yandex.ru/media/id/[id]/[article-title]`
- `https://dzen.ru/media/[channel]/[article-title]`

All three domains are supported: `zen.yandex.ru`, `dzen.ru`, `zen.yandex.com`

## Features in Detail

### URL Validation
The application validates that:
- The URL includes a proper protocol (http/https)
- The URL is from a recognized Yandex Zen domain
- The URL format is correct

### Article Extraction
The parser uses intelligent multi-method extraction to get **only the article text**, filtering out navigation, ads, comments, and other page elements:

1. **JSON-LD Structured Data** (most accurate): Extracts article body from structured metadata
2. **Article Tag Analysis**: Precisely extracts content from HTML `<article>` elements while removing nested non-content
3. **Zen-Specific Selectors**: Uses Yandex Zen specific CSS selectors for better accuracy
4. **Smart Filtering**: Automatically removes:
   - Navigation menus, headers, and footers
   - Social sharing buttons and comments
   - Advertisements and promotional content
   - Related articles and sidebars
   - Cookie notices and popups
   - UI elements (buttons, labels, short texts)

The parser includes noise detection to filter out common UI phrases in both English and Russian (e.g., "Subscribe", "Подписаться", "Read more", "Читать далее")

### Error Handling
The application handles various error scenarios:
- **Invalid URLs**: Alerts when URL format is incorrect or not from Yandex Zen
- **Network Errors**: Handles connection timeouts and network issues
- **HTTP Errors**: Manages 404 (Not Found), 403 (Forbidden), and other HTTP errors
- **Parsing Errors**: Gracefully handles cases where article content cannot be extracted

## Troubleshooting

### Application doesn't start
- Ensure Python 3.8+ is installed: `python3 --version`
- Verify all dependencies are installed: `pip install -r requirements.txt`
- On macOS, ensure tkinter is available (usually comes with Python)

### No text extracted
- Verify the URL is correct and the article exists
- Check your internet connection
- The article structure might have changed; Yandex Zen occasionally updates their HTML structure

### macOS-specific issues
- If you get a "Python is not installed as a framework" error, you may need to use `pythonw` instead of `python3`
- Ensure you're using the system Python or a properly configured Python installation

### Connection errors
- Check your internet connection
- Some articles may be geo-restricted
- Yandex Zen might be blocking automated access (try waiting a few minutes)

## Technical Details

### Dependencies
- **requests**: For HTTP requests to fetch article pages
- **beautifulsoup4**: For parsing HTML content
- **lxml**: Parser for BeautifulSoup (faster and more robust)
- **tkinter**: GUI framework (included with Python)

### Architecture
The application follows a single-class architecture with the `ZenParserGUI` class handling:
- GUI creation and layout
- URL validation
- HTTP requests with proper headers
- HTML parsing and text extraction
- Clipboard operations
- Error handling and user feedback

### User Agent
The application uses a macOS Chrome user agent to ensure compatibility with Yandex Zen's servers.

## Limitations

- The parser relies on the current HTML structure of Yandex Zen. If Yandex changes their layout significantly, the parser may need updates.
- Some articles with heavy JavaScript rendering might not parse correctly
- Geo-restricted or subscriber-only content might not be accessible

## Future Enhancements

Potential improvements for future versions:
- Support for batch processing multiple URLs
- Export to various formats (TXT, PDF, etc.)
- Image extraction
- Selenium support for JavaScript-heavy pages
- Article metadata extraction (author, date, tags)

## Documentation

This project includes comprehensive documentation:

- **[README.md](README.md)** - Main documentation (English)
- **[README_RU.md](README_RU.md)** - Русская документация
- **[QUICKSTART.md](QUICKSTART.md)** - Quick start guide
- **[URL_FORMATS.md](URL_FORMATS.md)** - Supported URL formats (all formats explained)
- **[MACOS_SETUP.md](MACOS_SETUP.md)** - macOS-specific setup instructions
- **[EXAMPLES.md](EXAMPLES.md)** - Detailed usage examples
- **[PARSING_DETAILS.md](PARSING_DETAILS.md)** - How the parser works
- **[CHANGELOG.md](CHANGELOG.md)** - Version history and changes

## License

This project is provided under the MIT License. See [LICENSE](LICENSE) for details.

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## Support

If you encounter any issues or have questions, please open an issue in the repository.
