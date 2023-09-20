from make_full_link_array import make_full_link_array
from log_record_add import log_record_add
from log_record_expire import log_record_expire
from create_imprint import create_imprint
import time

def changes_check(url, log_path, imprint_path):
    link_array = make_full_link_array(url)
    try:
        with open(imprint_path, 'r') as file:
            imprint_text=file.read()
        file.close()
    except FileNotFoundError:
        file=open(imprint_path, 'w')
        with open(imprint_path, 'r') as file:
            imprint_text=file.read()
        file.close()
    imprint_array=imprint_text.splitlines()
    added_ads_array = [x for x in link_array if x not in imprint_array]
    expired_ads_array = [x for x in imprint_array if x not in link_array]
    if len(added_ads_array)>0:
        for link_element in added_ads_array:
            log_record_add(link_element, log_path)
            time.sleep(5)  
    if len(expired_ads_array)>0:
        for link_element in expired_ads_array:
            log_record_expire(link_element, log_path)
            time.sleep(10)  
    create_imprint(imprint_path, link_array)