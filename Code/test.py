import csv

def read_car_market_csv(path):
    with open(path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter='\t')
        for line in csv_reader:
            #print(line)
            print(line['price'])


read_car_market_csv('/Users/Martin/GitKraken/CarMarketCrawling/Data/Land_Rover_Range_Rover_Evoque.csv')