from selenium import webdriver
import logging


def car_details_to_dict(price='', info_string=''):
    if len(info_string.splitlines()) == 9:
        # defining car details to read out
        car_detail_data_set = {
            'price': 0,
            'mileage': 0,
            'construction_year': 0,
            'power': 0,
            'car_state': 'new',
            'car_owner': 0,
            'transmission': 'manual',
            'fuel': 'petrol',
            'fuel_consumption_per_100_km': 0}
        list_of_details = info_string.splitlines()
        car_detail_data_set['mileage'] = int(list_of_details[0].split(' ')[0].replace('.', ''))
        car_detail_data_set['construction_year'] = int(list_of_details[1].split('/')[1])

        car_detail_data_set['price'] = int(price.split(' ')[1].split(',')[0].replace('.', ''))

        return car_detail_data_set
    else:
        return print('Improper info string')


#initialization
num_max_pages = 3
driver = webdriver.Firefox()
dict_details = []

url = 'https://www.autoscout24.de/lst/land-rover/range-rover-evoque?' \
      'sort=standard&desc=0&prevownersid=1&eq=49&gear=A&ustate=' \
      'N%2CU&size=20&page=1&powerfrom=147&powertype=hp&cy=D&kmto=10000&fregfrom=2019&atype=C&fc=12&qry=&'

for n in range(1, num_max_pages+1):

    url = url.replace('page=1', 'page=' + str(n))
    print(url)
    driver.get(url) #open web browser with specific url

    prices = driver.find_elements_by_xpath('//span[@class="cldt-price sc-font-xl sc-font-bold"]')
    details = driver.find_elements_by_xpath('//ul[@data-item-name="vehicle-details"]')

    if len(prices) == len(details):
        for i in range(len(details)):
            car_detail = car_details_to_dict(prices[i].text, details[i].text)
            dict_details.append(car_detail)
    else:
        print('uneven array lengths of prices and details')

driver.close() #close web browser

with open('car_market_data.csv', 'w') as f:
    f.write('Mileage in km' + ',' + 'Price in € \n')

with open('car_market_data.csv', 'a') as f:
    for entry in dict_details:
        f.write(str(entry.get('mileage')) + ',' + str(entry.get('price')) + "\n")
