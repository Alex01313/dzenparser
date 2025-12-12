#!/usr/bin/env python3
"""
Test fetching with proper session handling
"""

import requests
from bs4 import BeautifulSoup
import time


def test_fetch_with_redirects(url):
    """Test fetching with redirect following"""
    print(f"Testing URL: {url}")
    print("=" * 80)
    
    # Create session
    session = requests.Session()
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
    })
    
    try:
        # Try with allow_redirects
        print("\n1. Fetching with redirects allowed...")
        response = session.get(url, timeout=15, allow_redirects=True)
        print(f"   Final URL: {response.url}")
        print(f"   Status: {response.status_code}")
        print(f"   Content-Length: {len(response.content)} bytes")
        print(f"   Redirects: {len(response.history)} redirect(s)")
        
        for i, r in enumerate(response.history):
            print(f"     Redirect {i+1}: {r.status_code} -> {r.headers.get('Location', 'unknown')[:80]}")
        
        # Parse the final page
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Check what we got
        print("\n2. Analyzing final page...")
        
        # Look for article
        article = soup.find('article')
        if article:
            print("   ✓ Found <article> tag")
            paragraphs = article.find_all('p')
            print(f"   Paragraphs: {len(paragraphs)}")
            if paragraphs:
                for i, p in enumerate(paragraphs[:3]):
                    text = p.get_text(strip=True)
                    if len(text) > 20:
                        print(f"   P{i+1}: {text[:100]}...")
        
        # Look for any paragraphs
        all_p = soup.find_all('p')
        meaningful_p = [p for p in all_p if len(p.get_text(strip=True)) > 30]
        print(f"\n   Total <p> tags: {len(all_p)}")
        print(f"   Meaningful paragraphs: {len(meaningful_p)}")
        
        if meaningful_p:
            print("\n   Sample paragraphs:")
            for i, p in enumerate(meaningful_p[:5]):
                text = p.get_text(strip=True)
                print(f"   {i+1}. {text[:100]}...")
        
        # Look for title
        h1 = soup.find('h1')
        if h1:
            print(f"\n   Title (h1): {h1.get_text(strip=True)}")
        
        # Check if it's still a redirect page
        scripts = soup.find_all('script')
        for script in scripts:
            script_text = script.string or ""
            if 'form.submit' in script_text or 'redirect' in script_text.lower():
                print("\n   ⚠ Warning: Page contains redirect script")
                print("   This is likely an auth/SSO page, not the article")
        
        # Check for meta tags
        print("\n3. Checking meta tags...")
        og_title = soup.find('meta', property='og:title')
        if og_title:
            print(f"   og:title: {og_title.get('content', '')[:80]}")
        
        og_desc = soup.find('meta', property='og:description')
        if og_desc:
            print(f"   og:description: {og_desc.get('content', '')[:100]}")
        
        # Save for inspection
        print("\n4. Saving HTML...")
        with open('/tmp/final_page.html', 'w', encoding='utf-8') as f:
            f.write(response.text)
        print("   Saved to: /tmp/final_page.html")
        
        print("\n" + "=" * 80)
        
        # Check if we got actual content
        if len(meaningful_p) > 3:
            print("✓ SUCCESS: Found article content!")
            return True
        else:
            print("✗ FAIL: No article content found (likely auth page)")
            return False
        
    except Exception as e:
        print(f"\n✗ Error: {e}")
        import traceback
        traceback.print_exc()
        return False


def try_alternative_url_format(article_id):
    """Try alternative URL formats"""
    print("\n" + "=" * 80)
    print("Trying alternative URL formats...")
    print("=" * 80)
    
    alternatives = [
        f"https://dzen.ru/a/{article_id}",
        f"https://zen.yandex.ru/a/{article_id}",
        f"https://dzen.ru/media/{article_id}",
        f"https://zen.yandex.ru/media/{article_id}",
    ]
    
    for url in alternatives:
        print(f"\nTrying: {url}")
        result = test_fetch_with_redirects(url)
        if result:
            print(f"✓ This URL works!")
            return url
        print()
    
    return None


if __name__ == "__main__":
    url = "https://dzen.ru/a/aTsmd_bGr2aapkGO"
    article_id = "aTsmd_bGr2aapkGO"
    
    # Try the original URL
    success = test_fetch_with_redirects(url)
    
    if not success:
        print("\n⚠ Original URL didn't work. Trying alternatives...")
        try_alternative_url_format(article_id)
