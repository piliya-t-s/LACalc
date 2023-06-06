from .res.ui_dialog import Ui_var_dialog
from PySide6.QtWidgets import QDialog


class VarDialog(QDialog, Ui_var_dialog):
    def __init__(self, name, val):
        super().__init__()
        self.setupUi(self)
        self.var_name.setText(str(name))
        self.var_value.setText(str(val))
        self.setWindowIcon(QtGui.QIcon('logo.ico'))
