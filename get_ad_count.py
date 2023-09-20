def get_ad_count(page):
    placeholder = ((page.find('section', class_='grey search-list listing-traits')).find('input', attrs={'name': 'c'})).get('value')
    return placeholder