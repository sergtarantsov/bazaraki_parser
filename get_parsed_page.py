import requests
from bs4 import BeautifulSoup

def get_parsed_page(url):
    page = requests.get(url)
    page_soup = BeautifulSoup(page.text, 'lxml')
    return page_soup