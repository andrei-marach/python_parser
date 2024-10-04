import logging
import requests
import bs4
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('wb')

#у селениума бывают два типа ожиданий : explicit - явные , implicit - неявные

# у вайлдберриз динамический контент на сайте и нужно юзать Селениум
# с помощью селениума будем добывать данные
# c помощью супа будем их парсить и производить действия
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
URI = "https://www.wildberries.ru/catalog/muzhchinam/odezhda/rubashki"


def get_source_code(URI: str) -> None:

    driver.get(url=URI)
    # time.sleep(10)
    while True:
        try:
            element = WebDriverWait(driver=driver, timeout=2)

def main() -> None:
    get_source_code(URI)

class Client():

    def __init__(self):
        self.session = requests.Session()
        self.session.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
            'Accept-Language': 'ru',
        }

    def load_page(self,page: int = None):
        url = 'https://serveradmin.ru'
        res = self.session.get(url=url)
        res.raise_for_status()
        return res.text

    def parse_page(self, text: str):
        soup = bs4.BeautifulSoup(text, 'lxml')
        container = soup.select('div')
        for block in container:
            self.parse_block(block=block)

    def parse_block(self, block):
        logger.info(block)
        logger.info('=' * 100)

    def run(self):
        text = self.load_page()
        self.parse_page(text=text)

# if __name__ == '__main__':
#     parser = Client()
#     parser.run()
if __name__ == '__main__':
    main()