#!/usr/bin/env python3
"""
Test script to verify article extraction improvements
"""

from bs4 import BeautifulSoup
import re


def clean_text(text):
    """Clean and format the extracted text"""
    if not text:
        return ""
    
    text = text.strip()
    
    # Remove excessive whitespace
    text = re.sub(r'\n{3,}', '\n\n', text)
    text = re.sub(r' {2,}', ' ', text)
    text = re.sub(r'\t+', ' ', text)
    
    # Remove lines that are just whitespace
    lines = text.split('\n')
    lines = [line.strip() for line in lines if line.strip()]
    text = '\n'.join(lines)
    
    return text


def is_noise_text(text):
    """Check if text is likely UI noise rather than article content"""
    text_lower = text.lower()
    
    # Common UI phrases to filter out
    noise_phrases = [
        'read more', 'click here', 'subscribe', 'share', 'comment',
        'следить', 'подписаться', 'поделиться', 'комментарий',
        'читать далее', 'показать', 'скрыть', 'загрузить',
        'cookie', 'privacy policy', 'terms of service',
        'все права защищены', 'copyright', '©'
    ]
    
    for phrase in noise_phrases:
        if phrase in text_lower:
            return True
    
    # Filter out very short texts (likely buttons or labels)
    if len(text) < 20:
        return True
    
    # Filter out texts that are mostly links
    if text.count('http') > 2:
        return True
    
    return False


def test_noise_filter():
    """Test the noise filtering function"""
    print("Testing noise filter...")
    
    # Should be filtered out
    noise_texts = [
        "Подписаться",
        "Click here for more",
        "Share on Facebook",
        "Читать далее",
        "© 2024",
        "Short",
        "http://link1.com http://link2.com http://link3.com"
    ]
    
    for text in noise_texts:
        result = is_noise_text(text)
        status = "✓" if result else "✗"
        print(f"  {status} Filtered: '{text}' -> {result}")
    
    # Should NOT be filtered out
    good_texts = [
        "This is a proper paragraph with meaningful content that should be included in the article.",
        "Это обычный параграф текста статьи, который должен быть включен в результат.",
    ]
    
    print("\nTesting good content...")
    for text in good_texts:
        result = is_noise_text(text)
        status = "✓" if not result else "✗"
        print(f"  {status} Kept: '{text[:50]}...' -> {not result}")


def test_html_cleaning():
    """Test HTML element removal"""
    print("\n\nTesting HTML cleaning...")
    
    html = """
    <html>
        <head><script>alert('test');</script></head>
        <body>
            <nav>Navigation menu</nav>
            <header>Header content</header>
            <article>
                <h1>Article Title</h1>
                <p>This is the first paragraph of the article.</p>
                <p>This is the second paragraph with more content.</p>
                <div class="social-share">Share this article</div>
                <p>This is the third paragraph of actual content.</p>
            </article>
            <aside>Related articles</aside>
            <footer>Footer content</footer>
        </body>
    </html>
    """
    
    soup = BeautifulSoup(html, 'html.parser')
    
    # Remove unwanted elements
    for tag in soup.find_all(['script', 'style', 'noscript', 'iframe', 'form']):
        tag.decompose()
    
    for selector in ['nav', 'header', 'footer', 'aside', 'menu']:
        for element in soup.find_all(selector):
            element.decompose()
    
    noise_patterns = ['social', 'share', 'comment', 'advertisement']
    for pattern in noise_patterns:
        for element in soup.find_all(class_=re.compile(pattern, re.I)):
            element.decompose()
    
    # Extract article content
    article = soup.find('article')
    if article:
        title = article.find('h1')
        paragraphs = article.find_all('p')
        
        print(f"  ✓ Title: {title.get_text(strip=True)}")
        print(f"  ✓ Found {len(paragraphs)} paragraphs")
        for i, p in enumerate(paragraphs, 1):
            text = p.get_text(strip=True)
            if text:
                print(f"    - Paragraph {i}: {text}")


def main():
    """Run all tests"""
    print("=" * 60)
    print("Article Extraction Improvement Tests")
    print("=" * 60)
    
    test_noise_filter()
    test_html_cleaning()
    
    print("\n" + "=" * 60)
    print("Tests completed!")
    print("=" * 60)


if __name__ == "__main__":
    main()
