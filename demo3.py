import random
import time
import numpy as np

from PyQt5 import QtCore, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import pandas as pd

asset_tgt = ['000001']
desti_path = './'

shift_num = 50
config = {}
config['close_px'] = dict(linewidth=0.7, label='close', color='#767676',secondary_y=True)
config['close_pxma'] = dict(linewidth=2, label='ma_close', color='#767676',secondary_y=True)
config['s49'] = dict(linewidth=2.3, label='s49', color='#FFFFFF', secondary_y=False)
config['s75'] = dict(linewidth=2.3, label='s75', color='#008080', secondary_y=False)
config['s100'] = dict(linewidth=2.3, label='s100', color='#FFFF00',secondary_y=False)
config['s150'] = dict(linewidth=4.5, label='s150', color='#FF0000',secondary_y=False)  # original_lwt==4
config['s200'] = dict(linewidth=4.5, label='s200', color='#000000',secondary_y=False)  # original_lwt==4
config['s300'] = dict(linewidth=2.1, label='s300', color='#800080',secondary_y=False)
config['s400'] = dict(linewidth=2.1, label='s400', color='#800080',secondary_y=False)
config['s500'] = dict(linewidth=2.1, label='s500', color='#800080',secondary_y=False)
config['s600'] = dict(linewidth=2.1, label='s600', color='#800000',secondary_y=False)
config['s800'] = dict(linewidth=2.1, label='s800', color='#993300',econdary_y=False)
config['s1000'] = dict(linewidth=4.5, label='s1000', color='#9090FF',secondary_y=False)  # original_lwt==4.2
config['s1500'] = dict(linewidth=2.1, label='s1500', color='#FF99CC',secondary_y=False)  # original_lwt==1.8
config['s2000'] = dict(linewidth=2.1, label='s2000', color='#FFCC99',secondary_y=False)  # original_lwt==1.8
config['s3000'] = dict(linewidth=4.5, label='s3000', color='#FF6600',secondary_y=False)  # original_lwt==4.2
config['ub'] = dict(linewidth=1.8, label='ub', color='#0000FF', secondary_y=False)
config['lb'] = dict(linewidth=1.8, label='lb', color='#0000FF', secondary_y=False)
config['x'] = dict(linewidth=0.5, label='0_hori', color='#000000', secondary_y=False)

plot_list = ['s1000', 's800', 's600', 's500', 's400', 's300', 's200', 's150', 's100', 's75', 's49', 'ub', 'lb', 'x']
df = pd.read_csv("000001_30_t4_out.csv")
df['x'] = 0
df.sort_values(by='date', axis=0, ascending=True, inplace=True)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.figure = Figure(figsize=(5, 3))
        self.canvas = FigureCanvas(self.figure)
        self.ax = self.figure.subplots()
        self.index = 0
        self.setCentralWidget(self.canvas)

        self.plot_list = ['s1000', 's800', 's600', 's500', 's400', 's300', 's200', 's150', 's100', 's75', 's49', 'ub', 'lb', 'x']
        df = pd.read_csv("000001_30_t4_out.csv")
        df['x'] = 0
        df.sort_values(by='date', axis=0, ascending=True, inplace=True)
        self.d = {i: df[i].tolist() for i in plot_list}

        ax = []  
        ay = [] 

        for key in self.d:
            ax = [i for i in range(len(self.d[key]))]  
            ay = self.d[key]  
            self.ax.plot(ax, ay, linewidth=config[key]['linewidth'], label=config[key]['label'], color=config[key]['color']) 
            aax = plt.gca()
            aax.invert_xaxis()  

        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.on_timeout)
        timer.start(100)

    def on_timeout(self):
        self.ax.set_xlim(self.index, self.index+100)
        self.index += 10
        # print(self.ax.xlim)
        # self.ax.imshow()
        self.canvas.draw()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.resize(640, 480)
    w.show()

    sys.exit(app.exec_())