from changes_check import changes_check
import os

#нужно прописать путь к данной папке в env, на MacOS и Linux это делает с помощью команды в терминале. Это позволяет выполнять код в кроне MacOS
#export PARSER_DIR="полный путь к папке"
base_directory = os.environ.get('PARSER_DIR')

#ссылка на готовый фильтр в базараки
main_link = 'https://www.bazaraki.com/car-motorbikes-boats-and-parts/cars-trucks-and-vans/body-type---7/year_max---69/year_min---60/?price_min=12500&price_max=20000'
#путь к файлу логов - в нем собираются новые и истекшие объявления
log_path = os.path.join(base_directory, 'data/log_file.csv')
#путь к файлу отпечатка - для сравнения нового списка объявлений с предыдущим запросом
imprint_path = os.path.join(base_directory, 'data/imprint.csv')

changes_check(main_link,log_path, imprint_path)