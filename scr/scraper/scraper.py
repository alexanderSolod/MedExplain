import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_yale_health_links(url, target_url="https://medicine.yale.edu"):
    """
    Scrape all unique links from a given webpage that start with the specified 
    target URL.

    This function sends a GET request to the provided URL, parses the HTML
    content of the page, and extracts all anchor tags. It then filters the URLs 
    to include only those that start with the specified target URL 
    (default is "https://medicine.yale.edu"). The unique URLs are returned
    in a sorted list.

    Args:
        url (str): The URL of the webpage to scrape.
        target_url (str, optional): The target URL to filter links by. 
                                    Defaults to "https://medicine.yale.edu".

    Returns:
        list: A sorted list of unique URLs that start with the target URL. 
              If the request fails, returns an empty list.

    Example:
        scrape_yale_health_links('https://news.yale.edu/topics/health-medicine')
        [
            'https://medicine.yale.edu/some-page', 
            'https://medicine.yale.edu/another-page'
        ]
    """
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        links = soup.find_all('a', href=True)

        urls = set()
        for link in links:
            href = link['href']
            if href.startswith(target_url) or href.startswith('http://medicine.yale.edu'):
                urls.add(href)  
        return sorted(urls)
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return []
    

def scrape_article_content(url):
    """
    Scrape text and image data from specified elements on a given webpage.

    Args:
        url (str): The URL of the webpage to scrape.

    Returns:
        dict: A dictionary containing the article title and the scraped HTML content.
    """
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find the article title
        title_element = soup.find('h1', class_='article-header__title')
        title = title_element.get_text(strip=False) if title_element else 'No title found'
        
        # Find the main content divs
        content_divs = soup.find_all('div', class_='article-content__item')
        
        
        return {
            'link': url,
            'title': title,
            'raw_html': content_divs[0],
            'text': content_divs[0].get_text(strip=True),
        }
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return {}

# Usage example
url_list = scrape_yale_health_links('https://news.yale.edu/topics/health-medicine')
