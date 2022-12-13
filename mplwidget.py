from PyQt5.QtWidgets import *

from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt


class MplWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        # self.canvas = FigureCanvas(Figure())
        # vertical_layout = QVBoxLayout()
        # vertical_layout.addWidget(self.canvas)
        # self.canvas.axes = self.canvas.figure.add_subplot(111)
        # self.setLayout(vertical_layout)

        vertical_layout = QVBoxLayout()
        self.figure = plt.figure()
        self.figure.patch.set_facecolor('None')

        self.canvas = FigureCanvas(self.figure)
        vertical_layout.addWidget(self.canvas)
        self.canvas.setStyleSheet("background-color:transparent;")
        self.canvas.axes = self.canvas.figure.add_subplot(111)
        self.canvas.axes.patch.set_alpha(0)
        self.setLayout(vertical_layout)
