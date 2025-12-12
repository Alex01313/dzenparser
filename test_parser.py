#!/usr/bin/env python3
"""
Simple test script to verify the Zen parser functionality
"""

import sys


def test_imports():
    """Test that all required imports are available"""
    print("Testing imports...")
    try:
        import tkinter as tk
        print("✓ tkinter imported successfully")
    except ImportError as e:
        print(f"✗ tkinter import failed: {e}")
        return False
    
    try:
        import requests
        print("✓ requests imported successfully")
    except ImportError as e:
        print(f"✗ requests import failed: {e}")
        return False
    
    try:
        from bs4 import BeautifulSoup
        print("✓ BeautifulSoup imported successfully")
    except ImportError as e:
        print(f"✗ BeautifulSoup import failed: {e}")
        return False
    
    return True


def test_url_validation():
    """Test URL validation logic"""
    print("\nTesting URL validation...")
    from zen_parser_gui import ZenParserGUI
    import tkinter as tk
    
    root = tk.Tk()
    root.withdraw()  # Hide the window
    app = ZenParserGUI(root)
    
    # Test valid URLs
    valid_urls = [
        "https://zen.yandex.ru/media/id/123/article-456",
        "https://dzen.ru/article/123",
        "http://zen.yandex.com/id/123"
    ]
    
    for url in valid_urls:
        is_valid, message = app.validate_url(url)
        if is_valid:
            print(f"✓ Valid URL accepted: {url}")
        else:
            print(f"✗ Valid URL rejected: {url} - {message}")
            return False
    
    # Test invalid URLs
    invalid_urls = [
        "not-a-url",
        "https://google.com",
        "zen.yandex.ru/article",  # Missing protocol
        ""
    ]
    
    for url in invalid_urls:
        is_valid, message = app.validate_url(url)
        if not is_valid:
            print(f"✓ Invalid URL rejected: {url}")
        else:
            print(f"✗ Invalid URL accepted: {url}")
            return False
    
    root.destroy()
    return True


def test_gui_creation():
    """Test that GUI can be created without errors"""
    print("\nTesting GUI creation...")
    try:
        from zen_parser_gui import ZenParserGUI
        import tkinter as tk
        
        root = tk.Tk()
        root.withdraw()  # Hide the window
        app = ZenParserGUI(root)
        
        # Check that key widgets exist
        assert hasattr(app, 'url_entry'), "url_entry widget missing"
        assert hasattr(app, 'text_display'), "text_display widget missing"
        assert hasattr(app, 'parse_button'), "parse_button widget missing"
        assert hasattr(app, 'copy_button'), "copy_button widget missing"
        
        print("✓ GUI created successfully with all required widgets")
        root.destroy()
        return True
    except Exception as e:
        print(f"✗ GUI creation failed: {e}")
        return False


def main():
    """Run all tests"""
    print("=" * 50)
    print("Yandex Zen Parser - Test Suite")
    print("=" * 50)
    
    tests = [
        test_imports,
        test_url_validation,
        test_gui_creation
    ]
    
    results = []
    for test in tests:
        try:
            result = test()
            results.append(result)
        except Exception as e:
            print(f"✗ Test {test.__name__} failed with exception: {e}")
            results.append(False)
    
    print("\n" + "=" * 50)
    print(f"Test Results: {sum(results)}/{len(results)} passed")
    print("=" * 50)
    
    if all(results):
        print("\n✓ All tests passed!")
        return 0
    else:
        print("\n✗ Some tests failed")
        return 1


if __name__ == "__main__":
    sys.exit(main())
