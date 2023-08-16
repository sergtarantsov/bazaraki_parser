from bs4 import BeautifulSoup

html_string = '<a class="value-chars" href="https://www.bazaraki.com/car-motorbikes-boats-and-parts/cars-trucks-and-vans/mitsubishi/mitsubishi-l200/seats---5/">5</a>'
element = BeautifulSoup(html_string, "html.parser")
print(element.text)