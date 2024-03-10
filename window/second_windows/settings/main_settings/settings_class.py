# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLayout,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)
from window.main_window import res_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(421, 177)
        icon = QIcon()
        icon.addFile(u":/icon/calculator-Freepik.png", QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.horizontalLayout = QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, 0, -1)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.push_button_main = QPushButton(Dialog)
        self.push_button_main.setObjectName(u"push_button_main")
        self.push_button_main.setMinimumSize(QSize(100, 40))

        self.verticalLayout.addWidget(self.push_button_main)

        self.push_button_setting_window = QPushButton(Dialog)
        self.push_button_setting_window.setObjectName(u"push_button_setting_window")
        self.push_button_setting_window.setMinimumSize(QSize(100, 40))

        self.verticalLayout.addWidget(self.push_button_setting_window)

        self.push_button_profile = QPushButton(Dialog)
        self.push_button_profile.setObjectName(u"push_button_profile")
        self.push_button_profile.setMinimumSize(QSize(100, 40))

        self.verticalLayout.addWidget(self.push_button_profile)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.widget)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.push_button_main.setText(QCoreApplication.translate("Dialog", u"\u041e\u0431\u0449\u0438\u0435", None))
        self.push_button_setting_window.setText(QCoreApplication.translate("Dialog", u"\u0418\u043d\u0442\u0435\u0440\u0444\u0435\u0439\u0441", None))
        self.push_button_profile.setText(QCoreApplication.translate("Dialog", u"\u041f\u0440\u043e\u0444\u0438\u043b\u044c", None))
    # retranslateUi

