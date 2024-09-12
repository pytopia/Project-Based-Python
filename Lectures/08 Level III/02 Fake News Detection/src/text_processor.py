from bs4 import BeautifulSoup
import re
from markdownify import markdownify as md
from web_scraper import send_request

def extract_body_content(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    body = soup.find("body")
    if body:
        for element in body.find_all(["script", "style", "meta", "noscript"]):
            element.decompose()
        return str(body)

def clean_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    for tag in soup.find_all():
        tag.replace_with_children()
    text_content = str(soup)
    return re.sub(r'\s+', ' ', text_content)

def prepare_context(links):
    context = ""
    for link in links:
        try:
            response = send_request(link)
            body = extract_body_content(response.text)
            content = clean_html(body)
            markdown_content = md(content)
            top_1000_words = " ".join(markdown_content.split()[:1000])
            context += top_1000_words + "\n\n"
        except Exception as e:
            print(f"Error processing link: {link}. Error: {e}")
    return context
