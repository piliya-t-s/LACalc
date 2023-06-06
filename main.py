from PySide6.QtWidgets import QApplication
from view.mainwindow import MainWindow
from model.model import MatrixApp
from model.controller import Controller
import sys


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow(app)
    mapp = MatrixApp()
    controller = Controller(mapp, main)
    main.show()
    app.exec()
