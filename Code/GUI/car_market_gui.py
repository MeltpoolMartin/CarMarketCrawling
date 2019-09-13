from selenium import webdriver
from PyQt5.uic import loadUiType
import sys, csv
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QSizePolicy, QWidget
from PyQt5.QtWidgets import QFileDialog
import numpy as np
from numpy import arange, sin, pi
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
    def compute_initial_figure(self):
        t = arange(0.0, 3.0, 0.01)
        s = sin(2*pi*t)
        self.axes.plot(t, s)


class CarMarketCrawling():
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.url = ""

    def crawl_website(self, url):
        xpath_price = '//span[@class="cldt-price sc-font-xl sc-font-bold"]'
        xpath_detail = '//ul[@data-item-name="vehicle-details"]'
        xpath_filter = '//span[@class="sc-tag__label"]'
        self.driver.get(url)
        self.detail = self.dirver.find_elements_by_xpath(xpath_price)
        self.detail = self.dirver.find_elements_by_xpath(xpath_detail)
        self.filter = self.dirver.find_elements_by_xpath(xpath_filter)
        self.driver.close()


class CarMarketCrawlingUI(QMain_Window, UI_main_window):
    def __init__(self):
        super(CarMarketCrawlingUI, self).__init__()
        self.setupUi(self)
        self.ui = QWidget(self)

        sc = PlottingCanvas(self.ui  , width=5, height=4, dpi=100)
        self.mplvl.addWidget(sc)

        # self.menuOpen.addAction(self.actionOpen)
        # self.actionOpen.triggered.connect(self.load_car_market_data)


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    main = CarMarketCrawlingUI()

    main.show()
    sys.exit(app.exec_())