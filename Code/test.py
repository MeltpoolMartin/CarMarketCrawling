import csv
import matplotlib.pyplot as plt
import numpy as np

def read_car_market_csv(path):
    car_market_data = []
    with open(path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter='\t')
        for line in csv_reader:
            car_market_data.append(line)
        return car_market_data

def plotting_car_data(car_data_list = [{}]):
    x = []
    y = []
    for car_data in car_data_list:
        x.append(car_data.get('mileage'))
        y.append(car_data.get('price'))
    plt.xlabel('Mileage in km')
    plt.ylabel('Price in Euro')
    plt.plot(x, y, 'ro')
    plt.show()

car_data = read_car_market_csv('/Users/Martin/GitKraken/CarMarketCrawling/Data/car_market_data.csv')
print(car_data)
plotting_car_data(car_data)
