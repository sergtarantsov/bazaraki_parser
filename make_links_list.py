def make_links_list(page):
    links = (page.find('ul', class_='list-simple__output js-list-simple__output')).find_all('a', class_='announcement-block__title')
    links_count = len(links)
    links_array=[]
    for i in range(links_count):
        links_array.append(f"https://www.bazaraki.com{links[i].get('href')}")
    return links_array