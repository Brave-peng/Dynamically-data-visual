import PyQt5
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow
import sys
from PyQt5 import uic
import logging
from mainUI import Ui_Form


class Main(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.logger = None
        self.file = None
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.inportButton.clicked.connect(self.open_file)
        self.ui.exitButton.clicked.connect(QCoreApplication.instance().quit)

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
        self.file, _ = QFileDialog.getOpenFileName(self, 'open file', 'c:\\')
        self.logger.info(f"{self.file} is loaded")
        print(f"{self.file} is loaded")


if __name__ == "__main__":
    App = QApplication(sys.argv)  # 创建QApplication对象，作为GUI主程序入口
    Main = Main()
    Main.show()  # 显示主窗体
    sys.exit(App.exec_())  # 循环中等待退出程序
