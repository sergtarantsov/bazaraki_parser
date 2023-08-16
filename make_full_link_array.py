from get_ad_count import get_ad_count
from make_links_list import make_links_list
from get_parsed_page import get_parsed_page

def make_full_link_array(url):
    page = get_parsed_page(url)
    ad_count = int(get_ad_count(page))
    pages_count = ad_count // 60 + 1
    full_link_array = []
    for i in range(pages_count):
        url_index = url + '&page=' + str(i+1)
        page = get_parsed_page(url_index)
        full_link_array = full_link_array + make_links_list(page)
    return full_link_array