import requests
from bs4 import BeautifulSoup

def get_page_count(page):
    placeholder = ((page.find('section', class_='grey search-list listing-traits')).find('input', attrs={'name': 'rubric'})).get('value')
    return placeholder