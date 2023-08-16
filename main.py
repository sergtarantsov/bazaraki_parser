from get_ad_count import get_ad_count
from get_parsed_page import get_parsed_page
from make_links_list import make_links_list
from make_full_link_array import make_full_link_array
from create_imprint import create_imprint
from changes_check import changes_check

main_link = 'https://www.bazaraki.com/car-motorbikes-boats-and-parts/cars-trucks-and-vans/body-type---7/year_max---66/year_min---61/?price_min=12500&price_max=20000'

changes_check(main_link,'imprint.csv')