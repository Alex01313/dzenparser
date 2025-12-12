#!/usr/bin/env python3
"""
Selenium-based parser for JavaScript-rendered Dzen pages
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time


class SeleniumZenParser:
    """Parser using Selenium for JavaScript-rendered pages"""
    
    def __init__(self, headless=True):
        """Initialize Selenium driver"""
        self.headless = headless
        self.driver = None
    
    def setup_driver(self):
        """Setup Chrome driver with options"""
        chrome_options = Options()
        
        if self.headless:
            chrome_options.add_argument('--headless')
        
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--window-size=1920,1080')
        chrome_options.add_argument('--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')
        
        # Disable images for faster loading
        prefs = {
            'profile.managed_default_content_settings.images': 2,
        }
        chrome_options.add_experimental_option('prefs', prefs)
        
        try:
            self.driver = webdriver.Chrome(options=chrome_options)
            self.driver.set_page_load_timeout(30)
            return True
        except Exception as e:
            print(f"Failed to initialize Chrome driver: {e}")
            return False
    
    def fetch_article(self, url):
        """Fetch article using Selenium"""
        if not self.driver:
            if not self.setup_driver():
                return None
        
        try:
            print(f"Loading page: {url}")
            self.driver.get(url)
            
            # Wait for content to load
            print("Waiting for content to render...")
            time.sleep(3)  # Give time for JavaScript to execute
            
            # Try to wait for article content
            try:
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.TAG_NAME, "article"))
                )
            except:
                print("No article tag found, proceeding anyway...")
            
            # Get page source after JavaScript execution
            page_source = self.driver.page_source
            
            print(f"Page source length: {len(page_source)} bytes")
            
            return page_source
            
        except Exception as e:
            print(f"Error fetching article: {e}")
            return None
    
    def parse_article(self, url):
        """Parse article and extract text"""
        page_source = self.fetch_article(url)
        
        if not page_source:
            return None
        
        # Parse with BeautifulSoup
        soup = BeautifulSoup(page_source, 'html.parser')
        
        # Extract article text
        article_parts = []
        
        # Look for article tag
        article = soup.find('article')
        if article:
            print("✓ Found article tag")
            
            # Get title
            title = article.find(['h1', 'h2'])
            if title:
                article_parts.append(title.get_text(strip=True))
                article_parts.append('\n\n')
            
            # Get paragraphs
            paragraphs = article.find_all('p')
            print(f"Found {len(paragraphs)} paragraphs")
            
            for p in paragraphs:
                text = p.get_text(strip=True)
                if text and len(text) > 20:
                    article_parts.append(text)
                    article_parts.append('\n\n')
        else:
            print("✗ No article tag found")
            
            # Try to find paragraphs anywhere
            all_p = soup.find_all('p')
            print(f"Found {len(all_p)} total paragraphs on page")
            
            for p in all_p:
                text = p.get_text(strip=True)
                if text and len(text) > 30:
                    article_parts.append(text)
                    article_parts.append('\n\n')
        
        article_text = ''.join(article_parts).strip()
        
        return article_text
    
    def close(self):
        """Close the driver"""
        if self.driver:
            self.driver.quit()
            self.driver = None


def test_selenium_parser(url):
    """Test the Selenium parser"""
    print("=" * 80)
    print("Testing Selenium Parser")
    print("=" * 80)
    
    parser = SeleniumZenParser(headless=True)
    
    try:
        article_text = parser.parse_article(url)
        
        if article_text:
            print("\n" + "=" * 80)
            print("SUCCESS! Article text extracted:")
            print("=" * 80)
            print(article_text[:500] + "...")
            print(f"\nTotal length: {len(article_text)} characters")
            return True
        else:
            print("\n✗ Failed to extract article text")
            return False
            
    finally:
        parser.close()


if __name__ == "__main__":
    url = "https://dzen.ru/a/aTsmd_bGr2aapkGO"
    test_selenium_parser(url)
