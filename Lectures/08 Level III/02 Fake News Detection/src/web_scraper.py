import urllib
import requests
from bs4 import BeautifulSoup
import re
from functools import cache

@cache
def send_request(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    return response

def extract_links(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    a_tags = soup.find_all('a', recursive=True)
    for a in a_tags:
        h3_tags = a.find_all('h3', recursive=True)
        for _ in h3_tags:
            href = a['href']
            match = re.search(r'url=(.*?)&', href)
            if match:
                yield match.group(1)

def search_google(query):
    encoded_query = urllib.parse.quote_plus(query)
    url = f"https://www.google.com/search?q={encoded_query}"
    response = send_request(url)
    return list(extract_links(response.text))
