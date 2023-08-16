import time
from parse_ad_details import parse_ad_details

def log_record_add(link, log_file):
    ad_details_array = parse_ad_details(link)
    with open(log_file, 'a') as file:
        file.write(f"{'Add'}; {time.ctime()}; {link}; {'; '.join(ad_details_array)};\n")
    file.close()