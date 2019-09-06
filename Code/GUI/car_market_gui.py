from PyQt5.uic import loadUiType
import sys, csv
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import (FigureCanvasQTAgg as FigureCanvas,
                                                NavigationToolbar2QT as NavigationToolbar)


UI_main_window, QMain_Window = loadUiType('gui.ui')


class CarMarketCarwlingUI(QMain_Window, UI_main_window):
    def __init__(self, ):
        super(CarMarketCarwlingUI, self).__init__()
        self.setupUi(self)
        self.csv_reader = []

        self.menuOpen.addAction(self.actionOpen)
        self.actionOpen.triggered.connect(self.open_file_name_dialog)

    def open_file_name_dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_path, file_type = QFileDialog.getOpenFileName(self, caption="Choose a *.csv file",
                                                           filter='*.csv', options=options)
        print(file_path)
        self.read_car_market_csv(file_path)

    def read_car_market_csv(self, path):
        with open(path, 'r') as csv_file:
            self.csv_reader = csv.DictReader(csv_file, delimiter='\t')
            for line in self.csv_reader:
                print(line)

    # def add_fig(self, name, fig):
    #     print(name, fig.text)
    #     self.fig_dict[name] = fig
    #     self.mplFigs.addItem(name)
    #
    # def add_plot(self):
    #     self.canvas = FigureCanvas(fig)
    #     self.mplvl.addWidget(self.canvas)
    #     self.canvas.draw()
    #     self.toolbar = NavigationToolbar(self.canvas,
    #                                      self, coordinates=True)
    #     self.addToolBar(self.toolbar)


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    main = CarMarketCarwlingUI()

    main.show()
    sys.exit(app.exec_())