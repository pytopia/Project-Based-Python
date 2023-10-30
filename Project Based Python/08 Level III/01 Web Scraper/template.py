import urllib.request
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self, site):
        # Add attributes to Scraper object
        pass

    def scrape(self):
        # Use request to send a request to the website and get Response object
        # Parse the response with UTF-8 encoding
        # Find all html tags with specific CSS class
        # Write the result to a html file
        pass

if __name__ == '__main__':
    url = "https://www.varzesh3.com/"
    Scraper(url).scrape()