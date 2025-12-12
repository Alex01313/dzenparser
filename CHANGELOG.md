# Changelog

All notable changes to the Yandex Zen Article Parser will be documented in this file.

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
