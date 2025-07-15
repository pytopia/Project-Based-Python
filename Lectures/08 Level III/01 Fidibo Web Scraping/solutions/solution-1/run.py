# Source Code Link:
# https://thecleverprogrammer.com/2020/10/01/web-scraper-with-python/

import urllib.request
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self, site):
        self.site = site

    def scrape(self):
        response = urllib.request.urlopen(self.site)
        html = response.read()
        parser = "html.parser"
        sp = BeautifulSoup(html, parser, from_encoding='UTF-8')
        html = sp.select('.league-standing')[0]

        with open('output/page.html', 'w') as f:
            f.write(str(html))

        print('html file is ready!')


if __name__ == '__main__':
    url = "https://www.varzesh3.com/"
    Scraper(url).scrape()
