# Changelog

All notable changes to the Yandex Zen Article Parser will be documented in this file.

## [1.1.2] - 2024-12-12

### Added - MAJOR FEATURE! 🚀
- **Selenium Support**: Parser can now handle JavaScript-rendered pages!
  - Added optional Selenium integration for dynamic content
  - GUI checkbox to enable/disable JavaScript rendering
  - Automatic ChromeDriver setup with optimized options
  - Headless browser mode for background processing
  - Fallback to regular parsing if Selenium not available

- **JavaScript Rendering Checkbox**: 
  - Toggle "Use JavaScript Rendering (Selenium)" in GUI
  - Only appears if Selenium is installed
  - Automatically suggests enabling when auth errors occur

### Added
- **Authentication Detection**: Parser now detects when articles require authentication
  - Detects redirects to Yandex SSO/Passport pages
  - Checks for suspiciously small pages (< 5KB)
  - Identifies authentication redirect scripts
  - Shows helpful error messages in both Russian and English

### Improved
- **Error Messages**: More informative messages when articles are inaccessible
  - Explains possible reasons (auth required, deleted, geo-restrictions, needs JavaScript)
  - Provides actionable suggestions including Selenium option
  - Links to documentation (DZEN_AUTH_ISSUE.md, SELENIUM_SETUP.md)

### Added Files
- `parse_with_selenium()` method for JavaScript rendering
- `zen_parser_selenium.py` - Standalone Selenium parser
- Comprehensive Selenium setup guide (SELENIUM_SETUP.md)
- `check_if_auth_required()` method to detect auth pages
- Debug scripts for troubleshooting (debug_url.py, test_real_fetch.py)
- Updated requirements.txt with `selenium>=4.15.0`

## [1.1.1] - 2024-12-12

### Fixed
- **Paste Functionality**: Fixed critical issue where Cmd+V and right-click paste didn't work in URL field
  - Added explicit keyboard shortcuts for macOS (Cmd+V, Cmd+C, Cmd+X, Cmd+A)
  - Added keyboard shortcuts for Windows/Linux (Ctrl+V, Ctrl+C, Ctrl+X, Ctrl+A)
  - Added context menu with Cut/Copy/Paste/Select All options
  - Right-click now shows context menu with paste option

### Added
- Context menu for URL entry field (accessible via right-click)
- Cross-platform keyboard shortcuts support
- `setup_url_entry_bindings()` method for proper clipboard operations

## [1.1.0] - 2024-12-12

### Added
- **Intelligent Article-Only Extraction**: Parser now extracts only the main article text, filtering out:
  - Navigation menus, headers, and footers
  - Social sharing buttons and widgets
  - Comments sections
  - Advertisements and promotional content
  - Related articles and recommendations
  - Cookie notices and popups
  - Sidebar content
  
- **Noise Detection**: Automatic filtering of UI elements with text matching common patterns:
  - English phrases: "Read more", "Click here", "Subscribe", "Share", etc.
  - Russian phrases: "Подписаться", "Поделиться", "Читать далее", etc.
  - Very short texts (likely buttons or labels)
  - Content with excessive links
  
- **Enhanced Extraction Methods**:
  - Priority-based extraction starting with most accurate method (JSON-LD)
  - Zen-specific CSS selectors for better content targeting
  - Improved paragraph filtering with length and quality checks
  - Better handling of nested article elements

- **Text Cleaning**: Advanced text cleanup including:
  - Removal of excessive whitespace
  - Proper line break handling
  - Tab character normalization
  - Empty line filtering

### Changed
- Extraction now prioritizes JSON-LD structured data for maximum accuracy
- Improved article tag parsing to exclude nested non-article content
- More aggressive filtering of non-content elements
- Better paragraph quality assessment (minimum length requirements)

### Technical Improvements
- Added `is_noise_text()` method for intelligent content filtering
- Added `clean_text()` method for consistent text formatting
- Improved HTML element decomposition before extraction
- Better handling of Yandex Zen-specific HTML structure

## [1.0.0] - 2024-12-12

### Added
- Initial release
- GUI interface using tkinter
- Basic article extraction from Yandex Zen
- URL validation
- Copy to clipboard functionality
- Error handling for network issues
- macOS support
- Comprehensive documentation
