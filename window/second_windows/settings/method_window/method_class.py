# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'method.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QLabel,
    QPushButton, QRadioButton, QSizePolicy, QStackedWidget,
    QTabWidget, QWidget)
from window.main_window import res_rc

class Ui_Mehod_dialog(object):
    def setupUi(self, Mehod_dialog):
        if not Mehod_dialog.objectName():
            Mehod_dialog.setObjectName(u"Mehod_dialog")
        Mehod_dialog.resize(412, 274)
        icon = QIcon()
        icon.addFile(u":/icon/calculator-Freepik.png", QSize(), QIcon.Normal, QIcon.Off)
        Mehod_dialog.setWindowIcon(icon)
        self.gridLayout_2 = QGridLayout(Mehod_dialog)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(3, 3, 3, 3)
        self.push_button_next = QPushButton(Mehod_dialog)
        self.push_button_next.setObjectName(u"push_button_next")
        self.push_button_next.setMaximumSize(QSize(30, 50))

        self.gridLayout_2.addWidget(self.push_button_next, 2, 4, 1, 1)

        self.push_button_close = QPushButton(Mehod_dialog)
        self.push_button_close.setObjectName(u"push_button_close")

        self.gridLayout_2.addWidget(self.push_button_close, 2, 2, 1, 1)

        self.stackedWidget = QStackedWidget(Mehod_dialog)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.method = QWidget()
        self.method.setObjectName(u"method")
        self.gridLayout = QGridLayout(self.method)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.method)
        self.tabWidget.setObjectName(u"tabWidget")
        self.Romanovsky = QWidget()
        self.Romanovsky.setObjectName(u"Romanovsky")
        self.Romanovsky.setStyleSheet(u"")
        self.tabWidget.addTab(self.Romanovsky, "")
        self.Charlier = QWidget()
        self.Charlier.setObjectName(u"Charlier")
        self.tabWidget.addTab(self.Charlier, "")
        self.Dixon = QWidget()
        self.Dixon.setObjectName(u"Dixon")
        self.tabWidget.addTab(self.Dixon, "")

        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 2)

        self.stackedWidget.addWidget(self.method)
        self.significance_level = QWidget()
        self.significance_level.setObjectName(u"significance_level")
        self.gridLayout_3 = QGridLayout(self.significance_level)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.radio_button_095 = QRadioButton(self.significance_level)
        self.radio_button_095.setObjectName(u"radio_button_095")
        self.radio_button_095.setChecked(True)

        self.gridLayout_3.addWidget(self.radio_button_095, 1, 2, 1, 1)

        self.radio_button_098 = QRadioButton(self.significance_level)
        self.radio_button_098.setObjectName(u"radio_button_098")

        self.gridLayout_3.addWidget(self.radio_button_098, 1, 1, 1, 1)

        self.radio_button_099 = QRadioButton(self.significance_level)
        self.radio_button_099.setObjectName(u"radio_button_099")

        self.gridLayout_3.addWidget(self.radio_button_099, 1, 0, 1, 1)

        self.radio_button_09 = QRadioButton(self.significance_level)
        self.radio_button_09.setObjectName(u"radio_button_09")

        self.gridLayout_3.addWidget(self.radio_button_09, 1, 3, 1, 1)

        self.label = QLabel(self.significance_level)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 4)

        self.stackedWidget.addWidget(self.significance_level)

        self.gridLayout_2.addWidget(self.stackedWidget, 1, 1, 1, 4)

        self.push_button_save = QPushButton(Mehod_dialog)
        self.push_button_save.setObjectName(u"push_button_save")

        self.gridLayout_2.addWidget(self.push_button_save, 2, 1, 1, 1)

        self.push_button_back = QPushButton(Mehod_dialog)
        self.push_button_back.setObjectName(u"push_button_back")
        self.push_button_back.setMaximumSize(QSize(30, 50))

        self.gridLayout_2.addWidget(self.push_button_back, 2, 3, 1, 1)


        self.retranslateUi(Mehod_dialog)

        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        self.push_button_save.setDefault(True)


        QMetaObject.connectSlotsByName(Mehod_dialog)
    # setupUi

    def retranslateUi(self, Mehod_dialog):
        Mehod_dialog.setWindowTitle(QCoreApplication.translate("Mehod_dialog", u"\u0412\u044b\u0431\u043e\u0440 \u043c\u0435\u0442\u043e\u0434\u0430 \u0440\u0430\u0441\u0447\u0451\u0442\u0430", None))
        self.push_button_next.setText(QCoreApplication.translate("Mehod_dialog", u">", None))
        self.push_button_close.setText(QCoreApplication.translate("Mehod_dialog", u"\u0412\u044b\u0439\u0442\u0438", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Romanovsky), QCoreApplication.translate("Mehod_dialog", u"\u041c\u0435\u0442\u043e\u0434 \u0420\u043e\u043c\u0430\u043d\u043e\u0432\u0441\u043a\u043e\u0433\u043e", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Charlier), QCoreApplication.translate("Mehod_dialog", u"\u041c\u0435\u0442\u043e\u0434 \u0428\u0430\u0440\u043b\u044c\u0435", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Dixon), QCoreApplication.translate("Mehod_dialog", u"\u041c\u0435\u0442\u043e\u0434 \u0414\u0438\u043a\u0441\u043e\u043d\u0430", None))
        self.radio_button_095.setText(QCoreApplication.translate("Mehod_dialog", u"0.95", None))
        self.radio_button_098.setText(QCoreApplication.translate("Mehod_dialog", u"0.98", None))
        self.radio_button_099.setText(QCoreApplication.translate("Mehod_dialog", u"0.99", None))
        self.radio_button_09.setText(QCoreApplication.translate("Mehod_dialog", u"0.9", None))
        self.label.setText(QCoreApplication.translate("Mehod_dialog", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0443\u0440\u043e\u0432\u0435\u043d\u044c \u0437\u043d\u0430\u0447\u0438\u043c\u043e\u0441\u0442\u0438 - p:", None))
        self.push_button_save.setText(QCoreApplication.translate("Mehod_dialog", u"\u0421\u043e\u0445\u0440\u043e\u043d\u0438\u0442\u044c", None))
        self.push_button_back.setText(QCoreApplication.translate("Mehod_dialog", u"<", None))
    # retranslateUi

