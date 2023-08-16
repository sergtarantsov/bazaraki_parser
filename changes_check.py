from make_full_link_array import make_full_link_array
from log_record_add import log_record_add
from log_record_expire import log_record_expire
from create_imprint import create_imprint
import time

def changes_check(url, imprint_file):
    link_array = make_full_link_array(url)
    with open(imprint_file, 'r') as file:
        imprint_text=file.read()
    file.close()
    imprint_array=imprint_text.splitlines()
    added_ads_array = [x for x in link_array if x not in imprint_array]
    expired_ads_array = [x for x in imprint_array if x not in link_array]
    if len(added_ads_array)>0:
        for link_element in added_ads_array:
            log_record_add(link_element, 'log_file.csv')
            time.sleep(5)  
    if len(expired_ads_array)>0:
        for link_element in expired_ads_array:
            log_record_expire(link_element, 'log_file.csv')
            time.sleep(10)  
    create_imprint('imprint.csv', link_array)