from selenium import webdriver
import matplotlib.pyplot as plt
import numpy as np
import csv
import os
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
        car_detail_data_set['mileage'] = handle_dash_in_text(list_of_details[0])
        #car_detail_data_set['construction_year'] = int(list_of_details[1].split('/')[1])
        car_detail_data_set['power'] = int(list_of_details[2].split('(')[1].split(' ')[0])
        #car_detail_data_set['car_owner'] = int(list_of_details[4].split(' ')[0])
        car_detail_data_set['transmission'] = list_of_details[5]
        car_detail_data_set['fuel'] = list_of_details[6]
        car_detail_data_set['fuel_consumption_per_100_km'] = list_of_details[7].split(' ')[0]

        car_detail_data_set['price'] = int(price.split(' ')[1].split(',')[0].replace('.', ''))

        return car_detail_data_set
    else:
        return print('Improper info string')


def handle_dash_in_text(text = ''):
    filtered_text = text.split(' ')[0]
    if filtered_text == '-':
        return '0'
    if filtered_text.find('.') != -1:
        return int(filtered_text.replace('.', ''))
    else:
        return int(filtered_text)


def plotting_car_data(car_data_list = [{}]):
    x = np.array([], dtype=int)
    y = np.array([], dtype=int)

    for car_data in car_data_list:
        x = np.append(x, [int(car_data.get('mileage'))])
        y = np.append(y, [int(car_data.get('price'))])

    #initialize plot
    plt.suptitle('Car Value Plot')
    plt.xlabel('Mileage in km')
    plt.ylabel('Price in €')
    plt.grid(True)
    plt.plot(x, y, 'bx')

    #set axis
    #plt.axis([np.amin(x), np.amax(x), np.amin(y), np.amax(y)])

    #show plot
    plt.show()


def writing_to_car_market_csv(path, car_data_list = [{}]):
    with open(os.path.join(path, 'car_market_data.csv'), 'w') as csv_file:
        fieldnames = ['mileage', 'price', 'construction_year', 'power', 'car_state', 'car_owner', 'transmission', 'fuel', 'fuel_consumption_per_100_km']
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter='\t')
        csv_writer.writeheader()
        for line in car_data_list:
            csv_writer.writerow(line)

def read_car_market_csv():
    with open(path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter='\t')
        for line in csv_reader:
            print(line)


#initialization
num_max_pages = 2
num_max_delta_km = 1
delta_km = 10000
driver = webdriver.Firefox()
dict_details = []

url = 'https://www.autoscout24.de/lst/land-rover/range-rover-evoque?sort=standard&desc=0&eq=140%2C155%2C23&gear=A&fuel=B&doorfrom=4&doorto=5&ustate=N%2CU&page=1&powerfrom=147&powertype=hp&cy=D&kmto=10000&ptype=M&atype=C'


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

writing_to_car_market_csv('/Users/Martin/GitKraken/CarMarketCrawling/Data', dict_details)

plotting_car_data(dict_details)
