# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QLineEdit, QSizePolicy, QVBoxLayout, QWidget)

class Ui_var_dialog(object):
    def setupUi(self, var_dialog):
        if not var_dialog.objectName():
            var_dialog.setObjectName(u"var_dialog")
        var_dialog.resize(400, 300)
        self.verticalLayout_2 = QVBoxLayout(var_dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.var_name = QLineEdit(var_dialog)
        self.var_name.setObjectName(u"var_name")
        self.var_name.setMinimumSize(QSize(0, 40))

        self.verticalLayout_2.addWidget(self.var_name)

        self.var_value = QLineEdit(var_dialog)
        self.var_value.setObjectName(u"var_value")
        self.var_value.setMinimumSize(QSize(0, 40))

        self.verticalLayout_2.addWidget(self.var_value)

        self.buttonBox = QDialogButtonBox(var_dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout_2.addWidget(self.buttonBox)


        self.retranslateUi(var_dialog)
        self.buttonBox.accepted.connect(var_dialog.accept)
        self.buttonBox.rejected.connect(var_dialog.reject)

        QMetaObject.connectSlotsByName(var_dialog)
    # setupUi

    def retranslateUi(self, var_dialog):
        var_dialog.setWindowTitle(QCoreApplication.translate("var_dialog", u"Dialog", None))
        self.var_name.setText(QCoreApplication.translate("var_dialog", u"`", None))
    # retranslateUi

