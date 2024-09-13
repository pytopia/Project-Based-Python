from bs4 import BeautifulSoup
import re

def clean_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    for tag in soup.find_all():
        tag.replace_with_children()
    text_content = str(soup)
    return re.sub(r'\s+', ' ', text_content)
