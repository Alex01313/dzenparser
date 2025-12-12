#!/usr/bin/env python3
"""
Test different Yandex Zen URL formats
"""

from urllib.parse import urlparse


def validate_url(url):
    """Validate if the URL is a valid Yandex Zen URL"""
    try:
        parsed = urlparse(url)
        if not parsed.scheme:
            return False, "URL must include http:// or https://"
        
        # Check if it's a Zen URL
        zen_domains = ['zen.yandex.ru', 'dzen.ru', 'zen.yandex.com']
        if not any(domain in parsed.netloc for domain in zen_domains):
            return False, "URL must be from Yandex Zen (zen.yandex.ru, dzen.ru, or zen.yandex.com)"
        
        return True, "Valid URL"
    except Exception as e:
        return False, f"Invalid URL format: {str(e)}"


def test_url_formats():
    """Test various URL formats"""
    print("=" * 70)
    print("Testing Yandex Zen URL Formats")
    print("=" * 70)
    
    # Various URL formats used by Yandex Zen / Dzen
    test_urls = [
        # Old format (zen.yandex.ru)
        ("https://zen.yandex.ru/media/id/5f6c9e8f7d0a2a6b1c8f9a0b/title-123", "Old format with media/id/"),
        ("https://zen.yandex.ru/media/example/article-title-123456", "Old format with media/name/"),
        
        # New short format (dzen.ru)
        ("https://dzen.ru/a/aTsmd_bGr2aapkGO", "New short format /a/"),
        ("https://dzen.ru/a/ZAbCdEfGhIjKlMnO", "New short format (example)"),
        
        # Channel/profile URLs
        ("https://dzen.ru/id/5f6c9e8f7d0a2a6b1c8f9a0b", "Channel ID format"),
        ("https://zen.yandex.ru/id/username", "Old channel format"),
        
        # Alternative formats
        ("https://zen.yandex.com/media/id/123/article-456", "zen.yandex.com domain"),
        ("https://dzen.ru/media/id/123/article-789", "dzen.ru with media path"),
        
        # Edge cases
        ("http://dzen.ru/a/test123", "HTTP (not HTTPS)"),
        ("https://dzen.ru/", "Root URL only"),
        
        # Invalid URLs
        ("dzen.ru/a/test", "Missing protocol"),
        ("https://google.com/article", "Wrong domain"),
        ("https://zen.yandex.ru", "No article path"),
    ]
    
    print("\nTesting URL validation:\n")
    
    for url, description in test_urls:
        is_valid, message = validate_url(url)
        status = "✓ VALID" if is_valid else "✗ INVALID"
        color = '\033[92m' if is_valid else '\033[91m'
        reset = '\033[0m'
        
        print(f"{color}{status}{reset} | {description}")
        print(f"         URL: {url}")
        if not is_valid:
            print(f"         Reason: {message}")
        print()
    
    print("=" * 70)
    
    # Summary
    valid_count = sum(1 for url, _ in test_urls if validate_url(url)[0])
    print(f"\nSummary: {valid_count}/{len(test_urls)} URLs passed validation")
    print("=" * 70)


def analyze_short_url():
    """Analyze the specific short URL format"""
    print("\n" + "=" * 70)
    print("Analyzing Short URL Format: https://dzen.ru/a/...")
    print("=" * 70)
    
    url = "https://dzen.ru/a/aTsmd_bGr2aapkGO"
    parsed = urlparse(url)
    
    print(f"\nURL: {url}")
    print(f"  Scheme: {parsed.scheme}")
    print(f"  Domain: {parsed.netloc}")
    print(f"  Path: {parsed.path}")
    print(f"  Path segments: {parsed.path.split('/')}")
    
    # Check validation
    is_valid, message = validate_url(url)
    print(f"\n  Validation: {'✓ PASS' if is_valid else '✗ FAIL'}")
    print(f"  Message: {message}")
    
    print("\n" + "=" * 70)
    print("\nConclusion:")
    print("  The short URL format 'https://dzen.ru/a/...' is SUPPORTED!")
    print("  The parser should work with this URL format.")
    print("=" * 70)


if __name__ == "__main__":
    test_url_formats()
    analyze_short_url()
