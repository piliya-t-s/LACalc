import numpy as np
from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Qt

from model.model import MatrixApp
from view.dialog import VarDialog


class Controller:
    def __init__(self, model: MatrixApp, view: QMainWindow):
        self.model = model
        self.view = view
        self.view.input_line.textChanged.connect(self.update_app)
        self.view.add_button.clicked.connect(self.add_var_dialog)
        self.view.variable_list.itemDoubleClicked.connect(self.add_var_dialog)
        self.view.del_button.clicked.connect(self.del_var_clicked)

    def update_app(self):
        self.model.expression = self.view.input_line.text()
        self.model.update()
        self.view.result_panel.setText(str(self.model.result))

    def del_var_clicked(self):
        listItems = self.view.variable_list.selectedItems()
        if not listItems:
            return
        for item in listItems:
            print(item.text())
            self.model.del_variable(item.text())
            self.view.variable_list.takeItem(self.view.variable_list.row(item))

        self.update_app()

    def add_var_dialog(self, item=None):
        if not item:
            dlg = VarDialog("Name", "Value")
        else:
            value = self.model.values[item.text()]
            if isinstance(value, np.ndarray | np.generic):
                value = np.array2string(value, separator=",")
            else:
                value = str(value)
            dlg = VarDialog(item.text(), value)
        dlg.setWindowTitle("Edit variable")

        button = dlg.exec()

        if button:
            try:
                var_name = dlg.var_name.text()
                self.model.set_variable(var_name, dlg.var_value.text())
                if not self.view.variable_list.findItems(var_name, Qt.MatchFlag.MatchExactly):
                    self.view.variable_list.addItem(var_name)
            except ValueError as e:
                self.model.result = e

            self.update_app()
