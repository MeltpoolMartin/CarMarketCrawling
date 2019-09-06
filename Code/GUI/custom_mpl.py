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
        self.fig_dict = {}

        self.mplFigs.itemClicked.connect(self.change_fig)
        fig = Figure()
        self.add_mpl(fig)

    def change_fig(self, item):
        text = item.text()
        self.remove_mpl()
        self.add_mpl(self.fig_dict[text])

    def add_fig(self, name, fig):
        print(name, fig.text)
        self.fig_dict[name] = fig
        self.mplFigs.addItem(name)

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
    ax1f1 = fig1.add_subplot(111)
    ax1f1.plot(np.random.rand(5))

    fig2 = Figure()
    ax1f2 = fig2.add_subplot(121)
    ax1f2.plot(np.random.rand(5))
    ax2f2 = fig2.add_subplot(122)
    ax2f2.plot(np.random.rand(10))

    fig3 = Figure()
    ax1f3 = fig3.add_subplot(111)
    ax1f3.pcolormesh(np.random.rand(20, 20))

    app = QtWidgets.QApplication(sys.argv)
    main = Main()
    main.add_fig('One plot', fig1)
    main.add_fig('Two plots', fig2)
    main.add_fig('Pcolormesh', fig3)
    main.show()
    sys.exit(app.exec_())