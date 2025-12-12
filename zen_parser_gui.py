#!/usr/bin/env python3
"""
Yandex Zen Article Parser with GUI
A macOS-compatible application to extract article text from Yandex Zen articles.
"""

import tkinter as tk
from tkinter import scrolledtext, messagebox, ttk
import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urlparse
import sys


class ZenParserGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Yandex Zen Article Parser")
        self.root.geometry("900x700")
        
        # Configure style
        self.setup_styles()
        
        # Create GUI elements
        self.create_widgets()
        
        # Session for requests
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        })
    
    def setup_styles(self):
        """Setup the styling for the application"""
        style = ttk.Style()
        style.theme_use('default')
        
        # Configure colors
        bg_color = '#f0f0f0'
        self.root.configure(bg=bg_color)
    
    def create_widgets(self):
        """Create and layout all GUI widgets"""
        # Main container with padding
        main_frame = tk.Frame(self.root, bg='#f0f0f0', padx=20, pady=20)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title
        title_label = tk.Label(
            main_frame,
            text="Yandex Zen Article Parser",
            font=('Arial', 18, 'bold'),
            bg='#f0f0f0',
            fg='#333333'
        )
        title_label.pack(pady=(0, 20))
        
        # URL Input Frame
        url_frame = tk.Frame(main_frame, bg='#f0f0f0')
        url_frame.pack(fill=tk.X, pady=(0, 10))
        
        url_label = tk.Label(
            url_frame,
            text="Article URL:",
            font=('Arial', 12),
            bg='#f0f0f0',
            fg='#333333'
        )
        url_label.pack(side=tk.LEFT, padx=(0, 10))
        
        self.url_entry = tk.Entry(
            url_frame,
            font=('Arial', 11),
            relief=tk.SOLID,
            borderwidth=1
        )
        self.url_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        # Add context menu and keyboard shortcuts for URL entry
        self.setup_url_entry_bindings()
        
        # Buttons Frame
        buttons_frame = tk.Frame(main_frame, bg='#f0f0f0')
        buttons_frame.pack(fill=tk.X, pady=(0, 20))
        
        self.parse_button = tk.Button(
            buttons_frame,
            text="Parse Article",
            command=self.parse_article,
            font=('Arial', 12, 'bold'),
            bg='#4CAF50',
            fg='white',
            relief=tk.RAISED,
            borderwidth=2,
            padx=20,
            pady=8,
            cursor='hand2'
        )
        self.parse_button.pack(side=tk.LEFT, padx=(0, 10))
        
        self.copy_button = tk.Button(
            buttons_frame,
            text="Copy to Clipboard",
            command=self.copy_to_clipboard,
            font=('Arial', 12),
            bg='#2196F3',
            fg='white',
            relief=tk.RAISED,
            borderwidth=2,
            padx=20,
            pady=8,
            cursor='hand2'
        )
        self.copy_button.pack(side=tk.LEFT, padx=(0, 10))
        
        self.clear_button = tk.Button(
            buttons_frame,
            text="Clear",
            command=self.clear_text,
            font=('Arial', 12),
            bg='#f44336',
            fg='white',
            relief=tk.RAISED,
            borderwidth=2,
            padx=20,
            pady=8,
            cursor='hand2'
        )
        self.clear_button.pack(side=tk.LEFT)
        
        # Status Label
        self.status_label = tk.Label(
            main_frame,
            text="Ready",
            font=('Arial', 10),
            bg='#f0f0f0',
            fg='#666666',
            anchor='w'
        )
        self.status_label.pack(fill=tk.X, pady=(0, 10))
        
        # Text Display Area
        text_frame = tk.Frame(main_frame, bg='#f0f0f0')
        text_frame.pack(fill=tk.BOTH, expand=True)
        
        text_label = tk.Label(
            text_frame,
            text="Extracted Text:",
            font=('Arial', 12, 'bold'),
            bg='#f0f0f0',
            fg='#333333',
            anchor='w'
        )
        text_label.pack(fill=tk.X, pady=(0, 5))
        
        self.text_display = scrolledtext.ScrolledText(
            text_frame,
            wrap=tk.WORD,
            font=('Arial', 11),
            relief=tk.SOLID,
            borderwidth=1,
            padx=10,
            pady=10
        )
        self.text_display.pack(fill=tk.BOTH, expand=True)
        
        # Footer
        footer_label = tk.Label(
            main_frame,
            text="Compatible with macOS | Python 3.8+",
            font=('Arial', 9),
            bg='#f0f0f0',
            fg='#999999'
        )
        footer_label.pack(pady=(10, 0))
    
    def setup_url_entry_bindings(self):
        """Setup keyboard shortcuts and context menu for URL entry field"""
        # Create context menu for URL entry
        self.url_menu = tk.Menu(self.url_entry, tearoff=0)
        self.url_menu.add_command(label="Cut", command=lambda: self.url_entry.event_generate("<<Cut>>"))
        self.url_menu.add_command(label="Copy", command=lambda: self.url_entry.event_generate("<<Copy>>"))
        self.url_menu.add_command(label="Paste", command=lambda: self.url_entry.event_generate("<<Paste>>"))
        self.url_menu.add_separator()
        self.url_menu.add_command(label="Select All", command=lambda: self.url_entry.select_range(0, tk.END))
        
        # Bind right-click to show context menu
        def show_context_menu(event):
            try:
                self.url_menu.tk_popup(event.x_root, event.y_root)
            finally:
                self.url_menu.grab_release()
        
        self.url_entry.bind("<Button-3>", show_context_menu)  # Right-click
        self.url_entry.bind("<Button-2>", show_context_menu)  # Middle-click (alternative)
        
        # Bind keyboard shortcuts (macOS style)
        self.url_entry.bind("<Command-v>", lambda e: self.url_entry.event_generate("<<Paste>>"))
        self.url_entry.bind("<Command-c>", lambda e: self.url_entry.event_generate("<<Copy>>"))
        self.url_entry.bind("<Command-x>", lambda e: self.url_entry.event_generate("<<Cut>>"))
        self.url_entry.bind("<Command-a>", lambda e: self.url_entry.select_range(0, tk.END))
        
        # Also bind Control for non-Mac systems
        self.url_entry.bind("<Control-v>", lambda e: self.url_entry.event_generate("<<Paste>>"))
        self.url_entry.bind("<Control-c>", lambda e: self.url_entry.event_generate("<<Copy>>"))
        self.url_entry.bind("<Control-x>", lambda e: self.url_entry.event_generate("<<Cut>>"))
        self.url_entry.bind("<Control-a>", lambda e: self.url_entry.select_range(0, tk.END))
    
    def validate_url(self, url):
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
    
    def check_if_auth_required(self, response):
        """Check if the article requires authentication"""
        # Check if redirected to SSO/auth page
        if 'sso.passport.yandex.ru' in response.url or 'passport.yandex' in response.url:
            return True, "Redirected to Yandex authentication page"
        
        # Check if page is suspiciously small (likely a redirect page)
        if len(response.content) < 5000:
            return True, "Page too small - likely requires authentication or doesn't exist"
        
        # Check for auth-related content
        content_lower = response.content.lower()
        if b'form.submit()' in content_lower or b'sso.dzen.ru' in content_lower:
            return True, "Page contains authentication redirect"
        
        return False, "OK"
    
    def parse_article(self):
        """Parse the Yandex Zen article from the provided URL"""
        url = self.url_entry.get().strip()
        
        if not url:
            messagebox.showwarning("Input Required", "Please enter a Yandex Zen article URL")
            return
        
        # Validate URL
        is_valid, message = self.validate_url(url)
        if not is_valid:
            messagebox.showerror("Invalid URL", message)
            return
        
        # Update UI
        self.parse_button.config(state=tk.DISABLED)
        self.status_label.config(text="Fetching article...", fg='#2196F3')
        self.text_display.delete(1.0, tk.END)
        self.root.update()
        
        try:
            # Fetch the article
            response = self.session.get(url, timeout=10, allow_redirects=True)
            response.raise_for_status()
            
            # Check if article requires authentication
            auth_required, auth_message = self.check_if_auth_required(response)
            if auth_required:
                self.status_label.config(text="Authentication required", fg='#f44336')
                error_msg = (
                    "⚠️ Статья недоступна / Article Not Accessible\n\n"
                    f"{auth_message}\n\n"
                    "Возможные причины / Possible reasons:\n"
                    "• Статья требует авторизации / Requires authentication\n"
                    "• Статья удалена или не существует / Deleted or doesn't exist\n"
                    "• Географические ограничения / Geo-restrictions\n\n"
                    "Что попробовать / What to try:\n"
                    "1. Откройте ссылку в браузере / Open in browser\n"
                    "2. Попробуйте другую статью / Try another article\n"
                    "3. См. DZEN_AUTH_ISSUE.md / See DZEN_AUTH_ISSUE.md"
                )
                messagebox.showwarning("Authentication Required", error_msg)
                return
            
            # Parse the HTML
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Extract article content
            article_text = self.extract_article_text(soup)
            
            if article_text:
                # Display the extracted text
                self.text_display.insert(1.0, article_text)
                self.status_label.config(
                    text=f"Successfully extracted {len(article_text)} characters",
                    fg='#4CAF50'
                )
                messagebox.showinfo("Success", "Article parsed successfully!")
            else:
                self.status_label.config(text="No article content found", fg='#f44336')
                messagebox.showwarning(
                    "No Content",
                    "Could not extract article text. The page structure might have changed or the article may not be available."
                )
        
        except requests.exceptions.Timeout:
            self.status_label.config(text="Request timed out", fg='#f44336')
            messagebox.showerror("Timeout", "The request timed out. Please check your internet connection and try again.")
        
        except requests.exceptions.ConnectionError:
            self.status_label.config(text="Connection error", fg='#f44336')
            messagebox.showerror("Connection Error", "Could not connect to the server. Please check your internet connection.")
        
        except requests.exceptions.HTTPError as e:
            self.status_label.config(text=f"HTTP Error: {e.response.status_code}", fg='#f44336')
            if e.response.status_code == 404:
                messagebox.showerror("Not Found", "The article was not found (404). Please check the URL.")
            elif e.response.status_code == 403:
                messagebox.showerror("Access Denied", "Access to the article was denied (403). The content might be restricted.")
            else:
                messagebox.showerror("HTTP Error", f"HTTP Error {e.response.status_code}: {str(e)}")
        
        except Exception as e:
            self.status_label.config(text="Error occurred", fg='#f44336')
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
        
        finally:
            self.parse_button.config(state=tk.NORMAL)
    
    def extract_article_text(self, soup):
        """Extract article text from the parsed HTML - only the main article content"""
        article_parts = []
        
        # Remove unwanted elements from the entire soup first
        for tag in soup.find_all(['script', 'style', 'noscript', 'iframe', 'form']):
            tag.decompose()
        
        # Remove common non-article sections
        for selector in ['nav', 'header', 'footer', 'aside', 'menu']:
            for element in soup.find_all(selector):
                element.decompose()
        
        # Remove elements with common class patterns for navigation, ads, comments
        noise_patterns = [
            'navigation', 'nav', 'menu', 'sidebar', 'aside', 'footer', 'header',
            'comment', 'social', 'share', 'advertisement', 'ad-', 'promo',
            'related', 'recommend', 'popular', 'trending', 'subscribe',
            'cookie', 'banner', 'popup', 'modal'
        ]
        
        for pattern in noise_patterns:
            for element in soup.find_all(class_=re.compile(pattern, re.I)):
                element.decompose()
            for element in soup.find_all(id=re.compile(pattern, re.I)):
                element.decompose()
        
        # Method 1: Try JSON-LD structured data first (most accurate)
        json_ld_scripts = soup.find_all('script', type='application/ld+json')
        for json_ld in json_ld_scripts:
            try:
                import json
                data = json.loads(json_ld.string)
                
                # Handle both single objects and arrays
                if isinstance(data, list):
                    for item in data:
                        if isinstance(item, dict) and item.get('@type') in ['Article', 'NewsArticle', 'BlogPosting']:
                            data = item
                            break
                
                if isinstance(data, dict) and data.get('@type') in ['Article', 'NewsArticle', 'BlogPosting']:
                    # Extract headline/title
                    if 'headline' in data:
                        article_parts.append(data['headline'])
                        article_parts.append('\n\n')
                    
                    # Extract article body
                    if 'articleBody' in data and len(data['articleBody']) > 100:
                        article_parts.append(data['articleBody'])
                        return self.clean_text(''.join(article_parts))
            except:
                pass
        
        # Method 2: Look for article tag with specific content extraction
        article = soup.find('article')
        if article:
            # Clone the article to avoid modifying the original
            article_copy = article
            
            # Remove nested articles (like "related articles")
            for nested in article_copy.find_all('article'):
                if nested != article_copy:
                    nested.decompose()
            
            # Extract title from h1 or h2
            title = article_copy.find(['h1', 'h2'])
            if title:
                article_parts.append(title.get_text(strip=True))
                article_parts.append('\n\n')
                title.decompose()  # Remove to avoid duplication
            
            # Extract only paragraphs and headings (core content)
            for element in article_copy.find_all(['p', 'h3', 'h4', 'h5', 'h6']):
                # Check if the element is not inside a removed section
                text = element.get_text(strip=True)
                
                # Filter out short or suspicious content
                if text and len(text) > 15:
                    # Skip if it looks like a UI element or navigation
                    if not self.is_noise_text(text):
                        article_parts.append(text)
                        article_parts.append('\n\n')
        
        # Method 3: Look for specific Zen content containers
        if not article_parts:
            # Zen-specific selectors (more precise than generic divs)
            zen_selectors = [
                'div[class*="article-render"]',
                'div[class*="article__text"]',
                'div[class*="article-body"]',
                'div[class*="post-content"]',
                'div[class*="entry-content"]',
                'main article',
                'main[role="main"]'
            ]
            
            for selector in zen_selectors:
                try:
                    content = soup.select_one(selector)
                    if content:
                        # Extract title
                        title = content.find(['h1', 'h2'])
                        if title:
                            article_parts.append(title.get_text(strip=True))
                            article_parts.append('\n\n')
                            title.decompose()
                        
                        # Extract paragraphs
                        for p in content.find_all('p'):
                            text = p.get_text(strip=True)
                            if text and len(text) > 15 and not self.is_noise_text(text):
                                article_parts.append(text)
                                article_parts.append('\n\n')
                        
                        if article_parts:
                            break
                except:
                    continue
        
        # Method 4: Fallback - carefully extract from main content area
        if not article_parts:
            # Look for main tag or content-rich divs
            main_content = soup.find('main') or soup.find('div', id=re.compile(r'(main|content)', re.I))
            
            if main_content:
                # Get title
                title = main_content.find('h1')
                if title:
                    article_parts.append(title.get_text(strip=True))
                    article_parts.append('\n\n')
                
                # Get paragraphs from main content only
                paragraphs = main_content.find_all('p', recursive=True)
                for p in paragraphs:
                    # Check if paragraph is not inside excluded sections
                    if not any(parent.name in ['nav', 'aside', 'footer', 'header'] for parent in p.parents):
                        text = p.get_text(strip=True)
                        if text and len(text) > 30 and not self.is_noise_text(text):
                            article_parts.append(text)
                            article_parts.append('\n\n')
        
        return self.clean_text(''.join(article_parts))
    
    def is_noise_text(self, text):
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
    
    def clean_text(self, text):
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
    
    def copy_to_clipboard(self):
        """Copy the extracted text to clipboard"""
        text = self.text_display.get(1.0, tk.END).strip()
        
        if not text:
            messagebox.showwarning("No Content", "There is no text to copy. Please parse an article first.")
            return
        
        try:
            self.root.clipboard_clear()
            self.root.clipboard_append(text)
            self.root.update()
            self.status_label.config(text="Text copied to clipboard!", fg='#4CAF50')
            messagebox.showinfo("Success", "Text copied to clipboard!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to copy to clipboard: {str(e)}")
    
    def clear_text(self):
        """Clear the text display and URL entry"""
        self.text_display.delete(1.0, tk.END)
        self.url_entry.delete(0, tk.END)
        self.status_label.config(text="Ready", fg='#666666')


def main():
    """Main function to run the application"""
    root = tk.Tk()
    app = ZenParserGUI(root)
    
    # Center the window on screen
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f'{width}x{height}+{x}+{y}')
    
    root.mainloop()


if __name__ == "__main__":
    main()
