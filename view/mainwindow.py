from PySide6.QtWidgets import QMainWindow
from PySide6 import QtGui

from view.res.ui_main_window import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, app):
        super().__init__()
        self.setupUi(self)
        self.app = app
        self.setWindowIcon(QtGui.QIcon('logo.ico'))
        self.setWindowTitle("LACalc")
