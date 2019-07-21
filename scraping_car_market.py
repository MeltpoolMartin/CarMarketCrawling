from selenium import webdriver


def car_details_to_dict(price = 0, info_string = ''):
      if len(info_string.splitlines()) == 9:
            #defining car details to read out
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
            #car_detail_data_set['price'] = int Find a way to convert the price to an integer
            car_detail_data_set['mileage'] = int(list_of_details[0].split(' ')[1].replace('.', ''))
            car_detail_data_set['construction_year'] = int(list_of_details[2].split('/')[1])

            return car_detail_data_set
      else:
            return print('Improper info string')



url = 'https://www.autoscout24.de/lst/land-rover/range-rover-evoque?' \
      'sort=standard&desc=0&prevownersid=1&eq=49&gear=A&ustate=' \
      'N%2CU&size=20&page=1&powerfrom=147&powertype=hp&cy=D&kmto=10000&fregfrom=2019&atype=C&fc=12&qry=&'

driver = webdriver.Firefox()
driver.get(url) #open web browser with specific url

prices = driver.find_elements_by_xpath('//span[@class="cldt-price sc-font-xl sc-font-bold"]')
details = driver.find_elements_by_xpath('//ul[@data-item-name="vehicle-details"]')

if len(prices) == len(details):
      dict_details = []
      for detail in details:
            car_detail = car_details_to_dict(detail.text)
            print(car_detail)
            dict_details.append(car_detail)
print(dict_details)


driver.close() #close web browser


print(car_details_to_dict())