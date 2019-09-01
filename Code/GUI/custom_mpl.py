from PyQt5.uic import loadUiType
import sys
from PyQt5 import QtWidgets
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import (FigureCanvasQTAgg as FigureCanvas,
                                                NavigationToolbar2QT as NavigationToolbar)


UI_main_window, QMain_Window = loadUiType('gui.ui')


class Main(QMain_Window, UI_main_window):
    def __init__(self, ):
        super(Main, self).__init__()
        self.setupUi(self)

    def add_mpl(self, fig):
        self.canvas = FigureCanvas(fig)
        self.mplvl.addWidget(self.canvas)
        self.canvas.draw()
        self.toolbar = NavigationToolbar(self.canvas,
                                         self, coordinates=True)
        self.addToolBar(self.toolbar)

    def remove_mpl(self):
        self.mplvl.removeWidget(self.canvas)
        self.canvas.close()
        self.mplvl.removeWidget(self.toolbar)
        self.toolbar.close()


if __name__ == '__main__':

    fig1 = Figure()
    ax1f1 = fig1.add_subplot(111) # 111 means no positional arguments
    ax1f1.plot(np.random.rand(5))

    app = QtWidgets.QApplication(sys.argv)
    main = Main()
    main.add_mpl(fig1)
    #main.remove_mpl()
    main.show()
    sys.exit(app.exec_())