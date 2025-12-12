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
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            
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
        """Extract article text from the parsed HTML"""
        article_parts = []
        
        # Try multiple selectors for Yandex Zen content
        # Zen uses different structures, so we try various approaches
        
        # Method 1: Look for article tag
        article = soup.find('article')
        if article:
            # Remove script and style tags
            for tag in article.find_all(['script', 'style', 'noscript']):
                tag.decompose()
            
            # Extract title
            title = article.find(['h1', 'h2'])
            if title:
                article_parts.append(title.get_text(strip=True))
                article_parts.append('\n\n')
            
            # Extract paragraphs
            paragraphs = article.find_all('p')
            for p in paragraphs:
                text = p.get_text(strip=True)
                if text and len(text) > 20:  # Filter out very short paragraphs
                    article_parts.append(text)
                    article_parts.append('\n\n')
        
        # Method 2: Look for specific Zen classes/divs
        if not article_parts:
            # Try to find content by common class names
            content_divs = soup.find_all('div', class_=re.compile(r'(article|content|text|post)'))
            for div in content_divs:
                for tag in div.find_all(['script', 'style', 'noscript']):
                    tag.decompose()
                
                text = div.get_text(strip=True)
                if len(text) > 100:  # Only consider substantial content
                    article_parts.append(text)
                    break
        
        # Method 3: Try JSON-LD structured data
        if not article_parts:
            json_ld = soup.find('script', type='application/ld+json')
            if json_ld:
                try:
                    import json
                    data = json.loads(json_ld.string)
                    if isinstance(data, dict):
                        if 'articleBody' in data:
                            article_parts.append(data['articleBody'])
                        elif 'description' in data:
                            article_parts.append(data['description'])
                except:
                    pass
        
        # Method 4: Fallback - extract all meaningful paragraphs from the page
        if not article_parts:
            all_paragraphs = soup.find_all('p')
            for p in all_paragraphs:
                text = p.get_text(strip=True)
                if text and len(text) > 30:
                    article_parts.append(text)
                    article_parts.append('\n\n')
        
        # Clean and join the text
        article_text = ''.join(article_parts).strip()
        
        # Remove excessive whitespace
        article_text = re.sub(r'\n{3,}', '\n\n', article_text)
        article_text = re.sub(r' {2,}', ' ', article_text)
        
        return article_text
    
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
