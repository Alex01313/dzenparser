#!/usr/bin/env python3
"""
Debug script to analyze why a specific URL doesn't parse
"""

import requests
from bs4 import BeautifulSoup
import json


def debug_url(url):
    """Debug a specific URL to see what's available"""
    print(f"Debugging URL: {url}")
    print("=" * 80)
    
    # Setup session with headers
    session = requests.Session()
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    })
    
    try:
        # Fetch the page
        print("\n1. Fetching page...")
        response = session.get(url, timeout=10)
        response.raise_for_status()
        print(f"   Status: {response.status_code}")
        print(f"   Content-Type: {response.headers.get('Content-Type')}")
        print(f"   Content-Length: {len(response.content)} bytes")
        
        # Parse HTML
        print("\n2. Parsing HTML...")
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Check for article tag
        print("\n3. Looking for <article> tag...")
        article = soup.find('article')
        if article:
            print("   ✓ Found <article> tag")
            print(f"   Classes: {article.get('class', [])}")
            print(f"   ID: {article.get('id', 'none')}")
            paragraphs = article.find_all('p')
            print(f"   Paragraphs inside: {len(paragraphs)}")
            if paragraphs:
                print(f"   First paragraph preview: {paragraphs[0].get_text(strip=True)[:100]}...")
        else:
            print("   ✗ No <article> tag found")
        
        # Check for JSON-LD
        print("\n4. Looking for JSON-LD structured data...")
        json_ld_scripts = soup.find_all('script', type='application/ld+json')
        if json_ld_scripts:
            print(f"   ✓ Found {len(json_ld_scripts)} JSON-LD script(s)")
            for i, script in enumerate(json_ld_scripts):
                try:
                    data = json.loads(script.string)
                    print(f"   Script {i+1}:")
                    if isinstance(data, dict):
                        print(f"     @type: {data.get('@type', 'unknown')}")
                        if 'headline' in data:
                            print(f"     headline: {data.get('headline', '')[:80]}...")
                        if 'articleBody' in data:
                            body = data.get('articleBody', '')
                            print(f"     articleBody length: {len(body)} chars")
                            print(f"     articleBody preview: {body[:100]}...")
                    elif isinstance(data, list):
                        print(f"     List with {len(data)} items")
                        for item in data:
                            if isinstance(item, dict):
                                print(f"       - @type: {item.get('@type', 'unknown')}")
                except:
                    print(f"   Script {i+1}: Failed to parse JSON")
        else:
            print("   ✗ No JSON-LD scripts found")
        
        # Check for common content divs
        print("\n5. Looking for content divs...")
        content_patterns = [
            'article-render',
            'article__text',
            'article-body',
            'post-content',
            'entry-content'
        ]
        
        for pattern in content_patterns:
            divs = soup.find_all('div', class_=lambda x: x and pattern in str(x).lower())
            if divs:
                print(f"   ✓ Found {len(divs)} div(s) with class containing '{pattern}'")
                for div in divs[:2]:  # Show first 2
                    text = div.get_text(strip=True)
                    print(f"     Preview: {text[:80]}...")
        
        # Check for main tag
        print("\n6. Looking for <main> tag...")
        main = soup.find('main')
        if main:
            print("   ✓ Found <main> tag")
            paragraphs = main.find_all('p')
            print(f"   Paragraphs inside: {len(paragraphs)}")
            if paragraphs:
                print(f"   First paragraph: {paragraphs[0].get_text(strip=True)[:100]}...")
        else:
            print("   ✗ No <main> tag found")
        
        # Check all paragraphs
        print("\n7. Checking all <p> tags on page...")
        all_paragraphs = soup.find_all('p')
        print(f"   Total paragraphs found: {len(all_paragraphs)}")
        
        # Filter meaningful paragraphs
        meaningful = [p for p in all_paragraphs if len(p.get_text(strip=True)) > 30]
        print(f"   Meaningful paragraphs (>30 chars): {len(meaningful)}")
        
        if meaningful:
            print("\n   First 3 meaningful paragraphs:")
            for i, p in enumerate(meaningful[:3]):
                text = p.get_text(strip=True)
                print(f"   {i+1}. {text[:100]}...")
        
        # Check for title
        print("\n8. Looking for title...")
        title_tags = ['h1', 'h2']
        for tag in title_tags:
            titles = soup.find_all(tag)
            if titles:
                print(f"   ✓ Found {len(titles)} <{tag}> tag(s):")
                for t in titles[:3]:
                    print(f"     - {t.get_text(strip=True)[:80]}")
        
        # Save HTML for inspection
        print("\n9. Saving HTML for manual inspection...")
        with open('/tmp/debug_page.html', 'w', encoding='utf-8') as f:
            f.write(str(soup.prettify()))
        print("   Saved to: /tmp/debug_page.html")
        
        print("\n" + "=" * 80)
        print("Debug complete!")
        
    except Exception as e:
        print(f"\n✗ Error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    url = "https://dzen.ru/a/aTsmd_bGr2aapkGO"
    debug_url(url)
