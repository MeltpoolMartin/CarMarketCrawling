import csv
import matplotlib.pyplot as plt

def read_car_market_csv(path):
    car_market_data = []
    with open(path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter='\t')
        for line in csv_reader:
            car_market_data.append(line)
        return car_market_data

def plotting_car_data(car_data_list = [{}]):
    mileage_list = []
    price_list = []
    for car_data in car_data_list:
        mileage_list.append(car_data.get('mileage'))
        price_list.append(car_data.get('price'))
    plt.xlabel('Mileage in km')
    plt.ylabel('Price in Euro')
    plt.scatter(mileage_list, price_list)
    plt.show()

car_data = read_car_market_csv('/Users/Martin/GitKraken/CarMarketCrawling/Data/car_market_data.csv')
print(car_data)
plotting_car_data(car_data)
