from selenium import webdriver
from PyQt5.uic import loadUiType
import sys, csv
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QSizePolicy, QWidget
from PyQt5.QtWidgets import QFileDialog
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import (FigureCanvasQTAgg as FigureCanvas,
                                                NavigationToolbar2QT as NavigationToolbar)


UI_main_window, QMain_Window = loadUiType('gui.ui')


class CreateCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        self.compute_initial_figure()

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QtWidgets.QSizePolicy.Expanding,
                                   QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def compute_initial_figure(self):
        pass


class PlottingCanvas(CreateCanvas):
    def set_axes(self, x_label, y_label):
        self.axes.set_xlabel(x_label)
        self.axes.set_ylabel(y_label)

    def update_plt(self, x, y):
        self.axes.plot(x, y, 'bx')
        self.draw()


class CarMarketCrawling():
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.url = ""

    def crawl_website(self, url):
        xpath_price = '//span[@class="cldt-price plt-font-xl plt-font-bold"]'
        xpath_detail = '//ul[@data-item-name="vehicle-details"]'
        xpath_filter = '//span[@class="plt-tag__label"]'
        self.driver.get(url)
        self.detail = self.dirver.find_elements_by_xpath(xpath_price)
        self.detail = self.dirver.find_elements_by_xpath(xpath_detail)
        self.filter = self.dirver.find_elements_by_xpath(xpath_filter)
        self.driver.close()

    def car_details_to_dict(self, price, info_string):
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
            car_detail_data_set['mileage'] = self.handle_dash_in_text(list_of_details[0])
            # car_detail_data_set['construction_year'] = int(list_of_details[1].split('/')[1])
            car_detail_data_set['power'] = int(list_of_details[2].split('(')[1].split(' ')[0])
            # car_detail_data_set['car_owner'] = int(list_of_details[4].split(' ')[0])
            car_detail_data_set['transmission'] = list_of_details[5]
            car_detail_data_set['fuel'] = list_of_details[6]
            car_detail_data_set['fuel_consumption_per_100_km'] = list_of_details[7].split(' ')[0]

            car_detail_data_set['price'] = int(price.split(' ')[1].split(',')[0].replace('.', ''))

            return car_detail_data_set
        else:
            return print('Improper info string')


class CarMarketCrawlingUI(QMain_Window, UI_main_window):
    def __init__(self):
        super(CarMarketCrawlingUI, self).__init__()
        self.setupUi(self)
        self.ui = QWidget(self)

        self.plt = PlottingCanvas(self.ui, width=5, height=4, dpi=100)
        self.plt.set_axes(x_label='Mileage in km', y_label='Price in Euro')
        self.mplvl.addWidget(self.plt)

        self.menuOpen.addAction(self.actionOpen)
        self.actionOpen.triggered.connect(self.load_car_market_data)

    def file_dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getOpenFileName(self, "Car Market Crawling", "/Users/Martin/GitKraken/CarMarketCrawling/Data",
                                                   "*.csv", options=options)
        return file_name

    def load_car_market_data(self):
        mileage = []
        price = []
        car_data_list = read_car_market_csv(self.file_dialog())
        for line in car_data_list:
            mileage.append(int(line['mileage']))
            price.append(int(line['price']))
        self.plt.update_plt(mileage, price)


def read_car_market_csv(path):
    car_data_list = []
    with open(path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter='\t')
        for line in csv_reader:
            car_data_list.append(line)
    return car_data_list


def handle_dash_in_text(text):
    filtered_text = text.split(' ')[0]
    if filtered_text == '-':
        return '0'
    if filtered_text.find('.') != -1:
        return int(filtered_text.replace('.', ''))
    else:
        return int(filtered_text)


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    main = CarMarketCrawlingUI()

    main.show()
    sys.exit(app.exec_())