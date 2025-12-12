# Yandex Zen Article Parser

A Python GUI application for extracting article text from Yandex Zen (Дзен) articles. This application provides a user-friendly interface to parse and extract text content from Yandex Zen articles with support for macOS.

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

You can test the parser with Yandex Zen article URLs like:
- `https://zen.yandex.ru/media/...`
- `https://dzen.ru/...`

## Features in Detail

### URL Validation
The application validates that:
- The URL includes a proper protocol (http/https)
- The URL is from a recognized Yandex Zen domain
- The URL format is correct

### Article Extraction
The parser uses multiple methods to extract article content:
1. Searches for HTML `<article>` tags
2. Looks for common content class names
3. Attempts to parse JSON-LD structured data
4. Falls back to extracting all meaningful paragraphs

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

## License

This project is provided as-is for educational and personal use.

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## Support

If you encounter any issues or have questions, please open an issue in the repository.
