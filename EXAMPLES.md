# Usage Examples

This document provides practical examples of using the Yandex Zen Article Parser.

## Quick Start

### 1. First Time Setup

```bash
# Clone the repository
git clone <repository-url>
cd <repository-directory>

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate  # On macOS/Linux

# Install dependencies
pip install -r requirements.txt
```

### 2. Running the Application

**Option 1: Using the launcher script (Recommended for macOS)**
```bash
./run.sh
```

**Option 2: Direct execution**
```bash
# Make sure your virtual environment is activated
source venv/bin/activate
python3 zen_parser_gui.py
```

**Option 3: Using the shebang**
```bash
./zen_parser_gui.py
```

## Step-by-Step Usage

### Parsing an Article

1. **Launch the application**
   ```bash
   ./run.sh
   ```

2. **Copy a Yandex Zen article URL**
   - Go to zen.yandex.ru or dzen.ru
   - Find an article you want to parse
   - Copy the URL from your browser

3. **Paste the URL**
   - Click in the "Article URL" field
   - Paste the URL (Cmd+V on macOS)

4. **Parse the article**
   - Click the "Parse Article" button
   - Wait for the extraction to complete (usually 2-5 seconds)
   - The extracted text will appear in the text area

5. **Copy the extracted text**
   - Click "Copy to Clipboard" button
   - The text is now in your clipboard ready to paste elsewhere

### Example URLs Format

The parser supports all Yandex Zen / Dzen URL formats:

**✅ Short format (new, recommended):**
```
https://dzen.ru/a/aTsmd_bGr2aapkGO
https://dzen.ru/a/YbXz1234567890
https://dzen.ru/a/[any-article-id]
```

**✅ Long format (legacy):**
```
https://zen.yandex.ru/media/id/5f6c9e8f7d0a2a6b1c8f9a0b/title-slug-123
https://zen.yandex.ru/media/channelname/article-title
https://dzen.ru/media/example/article-title-123456
```

**✅ Alternative domains:**
```
https://zen.yandex.com/media/id/123/article-456
http://dzen.ru/a/test123  (HTTP also works)
```

All formats are fully supported!

## Troubleshooting Examples

### Problem: "Invalid URL" error

**Solution:** Ensure your URL:
- Starts with `http://` or `https://`
- Contains one of: `zen.yandex.ru`, `dzen.ru`, or `zen.yandex.com`

**Example of correct URL:**
```
https://zen.yandex.ru/media/id/5f6c9e8f7d0a2a6b1c8f9a0b/article-title
```

**Example of incorrect URL:**
```
zen.yandex.ru/media/id/5f6c9e8f7d0a2a6b1c8f9a0b/article-title  # Missing https://
https://google.com/article  # Wrong domain
```

### Problem: "No article content found"

**Possible causes:**
1. The article uses heavy JavaScript rendering
2. The article structure has changed
3. The URL is not actually an article page

**Solution:**
- Verify the URL points to an actual article (not a profile or channel page)
- Try a different article to confirm the parser is working
- Check if the article is accessible in a regular browser

### Problem: "Connection Error"

**Possible causes:**
1. No internet connection
2. Yandex Zen is blocking automated requests
3. The article is geo-restricted

**Solution:**
- Check your internet connection
- Wait a few minutes and try again
- Try accessing the article in a regular browser first

## Advanced Usage

### Running Tests

```bash
# Activate virtual environment
source venv/bin/activate

# Run the test suite (Note: GUI tests will fail without display)
python3 test_parser.py
```

### Checking Syntax

```bash
# Verify Python syntax is correct
python3 -m py_compile zen_parser_gui.py
```

### Verifying Dependencies

```bash
# Check if all packages are installed
python3 -c "import requests; from bs4 import BeautifulSoup; print('OK')"
```

## Tips and Best Practices

### For Best Results:

1. **Use full article URLs** - Don't use shortened URLs or redirects
2. **Wait for the status message** - The status label shows the progress
3. **Check the character count** - After parsing, the status shows how many characters were extracted
4. **Test with known articles first** - Verify the parser works with a few test articles

### Performance Tips:

1. **First parse may be slower** - The application needs to establish a connection
2. **Subsequent parses are faster** - The session is reused
3. **Large articles take longer** - Complex articles with lots of content need more processing time

### Common Workflows:

**Workflow 1: Research and Note-Taking**
```
1. Browse Yandex Zen articles
2. Find interesting articles
3. Parse each article
4. Copy text to your notes application
5. Repeat for multiple articles
```

**Workflow 2: Content Analysis**
```
1. Collect article URLs
2. Parse each article
3. Copy extracted text
4. Paste into analysis tool (word processor, analyzer, etc.)
```

## Error Messages Guide

| Error Message | Meaning | Solution |
|--------------|---------|----------|
| "Input Required" | No URL entered | Enter a valid URL |
| "Invalid URL" | URL format is wrong | Check URL format and domain |
| "Request timed out" | Connection timeout | Check internet, try again |
| "Connection Error" | Cannot connect | Verify internet connection |
| "Not Found (404)" | Article doesn't exist | Verify URL is correct |
| "Access Denied (403)" | Access blocked | Article may be restricted |
| "No article content found" | Parser couldn't extract text | Try a different article or check if article exists |

## Getting Help

If you encounter issues not covered here:

1. Check the main README.md for general information
2. Verify you're using Python 3.8 or higher
3. Ensure all dependencies are installed correctly
4. Try with a known working article URL first
5. Check the GitHub issues page for similar problems

## Example Session

Here's what a typical session looks like:

```
1. Launch: ./run.sh
   Output: "Starting Yandex Zen Article Parser..."
           "Launching GUI..."

2. GUI opens with title "Yandex Zen Article Parser"

3. Paste URL: https://zen.yandex.ru/media/...

4. Click "Parse Article"
   Status: "Fetching article..."
   Status: "Successfully extracted 2534 characters"
   Dialog: "Article parsed successfully!"

5. Click "Copy to Clipboard"
   Status: "Text copied to clipboard!"
   Dialog: "Text copied to clipboard!"

6. Text is now available to paste elsewhere (Cmd+V)

7. Click "Clear" to reset for next article
```

---

**Note:** This parser is designed for personal use. Please respect Yandex Zen's terms of service and robots.txt when using this tool.
