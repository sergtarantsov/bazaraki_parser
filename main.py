from changes_check import changes_check
import os

base_directory = os.environ.get('PARSER_DIR')
print(base_directory)
imprint_path = os.path.join(base_directory, 'data', 'imprint.csv')
print(imprint_path)

main_link = 'https://www.bazaraki.com/car-motorbikes-boats-and-parts/cars-trucks-and-vans/body-type---7/year_max---69/year_min---60/?price_min=12500&price_max=20000'

changes_check(main_link,imprint_path)