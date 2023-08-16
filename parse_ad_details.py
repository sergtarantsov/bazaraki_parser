from get_parsed_page import get_parsed_page

def parse_ad_details(link):
    ad_page=get_parsed_page(link)
    try:
        car=ad_page.find('h1', class_='title-announcement').text.replace('\n', '').replace('  ', '')
    except AttributeError:
        car=''
    post_date=ad_page.find('div', class_='announcement__details').find('span', class_='date-meta').text
    price=ad_page.find('div', class_='announcement-price__cost').text.split('\n')[3].replace(' ', '')
    try:
        start_price=ad_page.find('div', class_='announcement-price__discount').find('span').text.replace('\n', '').replace(' ', '')
    except AttributeError:
        start_price=''
    description=ad_page.find('head').find('meta', attrs={"name": "description"}).get('content').replace('\r\n', '   ').replace('\n', '  ').replace('\r', '  ')
    base = ad_page.find('div', class_= 'announcement-characteristics clearfix')
    base_elements=base.find_all('li')
    specs = []
    details_year=''
    details_doors=''
    details_drive=''
    details_power=''
    details_seats=''
    details_colour=''
    details_extras=''
    details_gearbox=''
    details_mileage=''
    details_mot=''
    details_body_type=''
    details_fuel=''
    details_engine_size=''
    for element in base_elements:
        first_element=(element.find(class_='key-chars')).text
        second_element=(element.find(class_='value-chars')).text
        if first_element == 'Year:':
            details_year=second_element  
        if first_element == 'Doors:':
            details_doors=second_element
        if first_element == 'Drive:':
            details_drive=second_element
        if first_element == 'Power:':
            details_power=second_element
        if first_element == 'Seats:':
            details_seats=second_element
        if first_element == 'Colour:':
            details_colour=second_element
        if first_element == 'Extras:':
            details_extras=second_element
        if first_element == 'Gearbox:':
            details_gearbox=second_element
        if first_element == 'Mileage (in km):':
            details_mileage=second_element
        if first_element == 'MOT till:':
            details_mot=second_element.replace('\n', '').replace('  ', '')
        if first_element == 'Body type:':
            details_body_type=second_element
        if first_element == 'Fuel type:':
            details_fuel=second_element
        if first_element == 'Engine size:':
            details_engine_size=second_element
    specs = [car, price, start_price, post_date, details_year, details_doors, details_drive, details_power, details_seats, details_colour, details_gearbox, details_mileage, details_mot, details_body_type, details_fuel, details_engine_size, details_extras, description]
    return(specs)