import time
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow, QWidget, QMessageBox
import sys
from PyQt5 import uic
import logging
from mainUI import Ui_Form
from PIL import Image, ImageQt
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure
import matplotlib.ticker as ticker


SHIFT_NUM = 10
SPEED = 10
WINDOW_LENGTH = 3000
TICK_SPACING = 100
Y_SIZE = 16
config = {}
config['close'] = dict(linewidth=0.7, label='close', color='#767676',secondary_y=True)
config['ma_close'] = dict(linewidth=2, label='ma_close', color='#767676',secondary_y=True)
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
plot_list = ['close', 'ma_close', 's1000', 's800', 's600', 's500', 's400', 's300', 's200', 's150', 's100', 's75', 's49', 'ub', 'lb', 'x']

class Main(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.logger = None
        self.index = 0
        self.init_looger()
        self.mirrow_flag = False
        self.d = {}
        self.play_flag = False
        self.file = None
        self.reverse_flag = False
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.horizontalSlider.setMaximum(10)
        self.ui.horizontalSlider.setMinimum(1)
        self.ui.horizontalSlider.setSingleStep(5)
        self.ui.inportButton.clicked.connect(self.open_file)
        self.ui.exitButton.clicked.connect(QCoreApplication.instance().quit)
        self.ui.playButton.clicked.connect(self.play)
        self.ui.stopButton.clicked.connect(self.stop)
        self.ui.reverseButton.clicked.connect(self.reverse)
        self.ui.mirrowButton.clicked.connect(self.mirrow)
        self.ui.jumpButton.clicked.connect(self.jump)

        self.figure = Figure(figsize=(10, 7), facecolor="gainsboro")
        self.canvas = FigureCanvas(self.figure)
        
        self.ax = self.figure.subplots()
        self.ax.patch.set_facecolor("gainsboro")
        self.twin_axes = self.ax.twinx().twiny()
        
        self.index = 0
        graphicscene = QtWidgets.QGraphicsScene()
        graphicscene.addWidget(self.canvas)
        self.ui.graphicsView.setScene(graphicscene)
        self.ui.graphicsView.show()

        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.on_timeout)
        timer.start(30)

        self.f1 = lambda bottom: bottom*0.95 if bottom > 0 else bottom*1.05
        self.f2 = lambda top: top*1.4 if top > 0 else top*0.7

    def on_timeout(self):
        if self.file is not None and self.play_flag:
            self.ax.set_xlim(self.index, self.index + WINDOW_LENGTH)
            top1, bottom1 = -float("inf"), float("inf")
            top2, bottom2 = -float("inf"), float("inf")
            for key in self.d:
                ay = self.d[key][self.index: self.index + WINDOW_LENGTH] 
                
                if key not in ['close', 'ma_close']:
                    top1 = max(top1, max(ay))
                    bottom1 = min(bottom1, min(ay))
                else:
                    top2 = max(top2, max(ay))
                    bottom2 = min(bottom2, min(ay))
            self.ax.set_ylim(self.f1(bottom1), self.f2(top1))
            self.ax.set_xticklabels(self.df.index.tolist()[self.index:self.index+WINDOW_LENGTH:TICK_SPACING], rotation=45, fontsize=6)        
            self.twin_axes.set_xlim(self.index, self.index + WINDOW_LENGTH)
            self.twin_axes.set_ylim(self.f1(bottom2), self.f2(top2))

            if not self.reverse_flag:
                self.index += SHIFT_NUM + self.ui.horizontalSlider.value() * SPEED
                self.check_border()
                self.canvas.draw()
            else:  
                self.index -= SHIFT_NUM + self.ui.horizontalSlider.value() * SPEED
                self.check_border()
                self.canvas.draw()

    def init_looger(self):
        logger = logging.getLogger("plot log")
        logger.setLevel(logging.INFO)
        cmd_logger = logging.StreamHandler()
        cmd_logger.setLevel(logging.INFO)
        fmt = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        cmd_logger.setFormatter(fmt)
        logger.addHandler((cmd_logger))
        self.logger = logger

    def open_file(self):
        self.file, _ = QFileDialog.getOpenFileName(self, 'open file', '.\\')
        if self.file is not None:
            self.logger.info(f"{self.file} is loaded")
            self.df = pd.read_csv(self.file, index_col='date')
            self.df['x'] = 0
            self.df.sort_values(by='date', axis=0, ascending=True, inplace=True)

            self.d = {i : self.df[i].tolist() for i in plot_list}
            ax = []  
            ay = [] 
            for key in self.d:
                ax = [i for i in range(len(self.d[key]))]  
                ay = self.d[key]  
                if key not in ['close', 'ma_close']:
                    self.ax.plot(ax, ay, linewidth=config[key]['linewidth'], label=config[key]['label'], color=config[key]['color']) 
                    aax = plt.gca()
                    aax.invert_xaxis()
                else:
                    self.twin_axes.plot(ax, ay, linewidth=config[key]['linewidth'], label=config[key]['label'], color=config[key]['color']) 
                    aax = plt.gca()
                    aax.invert_xaxis()  
            self.ax.set_xticklabels(self.df.index.tolist()[::TICK_SPACING], rotation=45, fontsize=6)
            self.ax.xaxis.set_major_locator(ticker.MultipleLocator(TICK_SPACING))
            self.ax.tick_params(labelsize=Y_SIZE)
            self.twin_axes.tick_params(labelsize=Y_SIZE)
        self.logger.info("初始化完毕")

    def check_border(self):
        if self.index + WINDOW_LENGTH >= len(self.d['s800']):
            self.index = len(self.d['s800']) - WINDOW_LENGTH
        if self.index <= 0:
            self.index = 0

    def play(self):
        self.reverse_flag = False
        self.play_flag = True

    def stop(self):
        self.play_flag = False

    def reverse(self):
        self.reverse_flag = True
        self.play_flag = True

    def mirrow(self):
        self.mirrow_flag = not self.mirrow_flag
        self.df = pd.read_csv(self.file, index_col='date')
        self.df = self.df if self.mirrow_flag == False else -self.df
        self.df['x'] = 0
        self.df.sort_values(by='date', axis=0, ascending=True, inplace=True)

        self.d = {i : self.df[i].tolist() for i in plot_list}
        ax = []  
        ay = [] 
        self.ax.clear()
        self.ax.patch.set_facecolor("gainsboro")
        for key in self.d:
            ax = [i for i in range(len(self.d[key]))]  
            ay = self.d[key]  
            if key not in ['close', 'ma_close']:
                self.ax.plot(ax, ay, linewidth=config[key]['linewidth'], label=config[key]['label'], color=config[key]['color']) 
                aax = plt.gca()
                aax.invert_xaxis()
            else:
                self.twin_axes.plot(ax, ay, linewidth=config[key]['linewidth'], label=config[key]['label'], color=config[key]['color']) 
                aax = plt.gca()
                aax.invert_xaxis() 
        self.ax.set_xlim(self.index, self.index + WINDOW_LENGTH)
        top1, bottom1 = -float("inf"), float("inf")
        top2, bottom2 = -float("inf"), float("inf")
        for key in self.d:
            ay = self.d[key][self.index: self.index + WINDOW_LENGTH] 
            
            if key not in ['close', 'ma_close']:
                top1 = max(top1, max(ay))
                bottom1 = min(bottom1, min(ay))
            else:
                top2 = max(top2, max(ay))
                bottom2 = min(bottom2, min(ay))
        self.ax.set_ylim(self.f1(bottom1), self.f2(top1))
        self.ax.set_xticklabels(self.df.index.tolist()[self.index:self.index+WINDOW_LENGTH:TICK_SPACING], rotation=45, fontsize=6)        
        self.twin_axes.set_xlim(self.index, self.index + WINDOW_LENGTH)
        self.twin_axes.set_ylim(self.f1(bottom2), self.f2(top2))
        if not self.reverse_flag:
            self.index += SHIFT_NUM + self.ui.horizontalSlider.value() * SPEED
            self.check_border()
            self.canvas.draw()
        else:  
            self.index -= SHIFT_NUM + self.ui.horizontalSlider.value() * SPEED
            self.check_border()
            self.canvas.draw()
        self.ax.set_xticklabels(self.df.index.tolist()[::TICK_SPACING], rotation=45, fontsize=6)
        self.ax.xaxis.set_major_locator(ticker.MultipleLocator(TICK_SPACING))
        self.ax.tick_params(labelsize=Y_SIZE)
        self.twin_axes.tick_params(labelsize=Y_SIZE)
        self.canvas.draw()

    def jump(self):
        text = self.ui.junpLine.text()
        l = self.df.index.to_list()
        target = -1
        for i, data in enumerate(l):
            if text in data:
                target = i
                break
        if target != -1:
            self.index = target
            self.ax.set_xlim(self.index, self.index + WINDOW_LENGTH)
            top1, bottom1 = -float("inf"), float("inf")
            top2, bottom2 = -float("inf"), float("inf")
            for key in self.d:
                ay = self.d[key][self.index: self.index + WINDOW_LENGTH] 
                
                if key not in ['close', 'ma_close']:
                    top1 = max(top1, max(ay))
                    bottom1 = min(bottom1, min(ay))
                else:
                    top2 = max(top2, max(ay))
                    bottom2 = min(bottom2, min(ay))
            self.ax.set_ylim(self.f1(bottom1), self.f2(top1))
            self.ax.set_xticklabels(self.df.index.tolist()[self.index:self.index+WINDOW_LENGTH:TICK_SPACING], rotation=45, fontsize=6)        
            self.twin_axes.set_xlim(self.index, self.index + WINDOW_LENGTH)
            self.twin_axes.set_ylim(self.f1(bottom2), self.f2(top2))
            if not self.reverse_flag:
                self.index += SHIFT_NUM + self.ui.horizontalSlider.value() * SPEED
                self.check_border()
                self.canvas.draw()
            else:  
                self.index -= SHIFT_NUM + self.ui.horizontalSlider.value() * SPEED
                self.check_border()
                self.canvas.draw()
            self.ax.tick_params(labelsize=Y_SIZE)
            self.twin_axes.tick_params(labelsize=Y_SIZE)            
            self.stop()
        else:
            QMessageBox.information(self, "信息提示", "未找到该日期")

        # input example

if __name__ == "__main__":
    App = QApplication(sys.argv)  # 创建QApplication对象，作为GUI主程序入口
    Main = Main()
    Main.show()  # 显示主窗体
    sys.exit(App.exec_())  # 循环中等待退出程序
