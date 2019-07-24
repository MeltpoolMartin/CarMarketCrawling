from selenium import webdriver
import matplotlib.pyplot as  plt
import logging


def car_details_to_dict(price='', info_string=''):
    print(info_string)
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


def plotting_car_data(car_data_list = [{}]):
    print(car_data_list)
    mileage_list = []
    price_list = []
    for car_data in car_data_list:
        mileage_list.append(car_data.get('mileage'))
        price_list.append(car_data.get('price'))
    plt.xlabel('Mileage in km')
    plt.ylabel('Price in Euro')
    plt.scatter(mileage_list, price_list)
    plt.show()


#initialization
num_max_pages = 3
num_max_delta_km = 3
delta_km = 10000
driver = webdriver.Firefox()
dict_details = []

url = 'https://www.autoscout24.de/lst/audi/q5?sort=standard&desc=0&gear=A&fuel=B&ustate=N%2CU&size=20&page=1&powerfrom=147&powertype=hp&cy=D&kmto=10000&kmfrom=0&fregfrom=2018&atype=C&'


for page in range(1, num_max_pages+1):

    url = url.replace('page=1', 'page=' + str(page))
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

plotting_car_data(dict_details)

# with open('car_market_data.csv', 'w') as f:
#     f.write('Mileage in km' + ',' + 'Price in € \n')
#
# with open('car_market_data.csv', 'a') as f:
#     for entry in dict_details:
#         f.write(str(entry.get('mileage')) + ',' + str(entry.get('price')) + "\n")
