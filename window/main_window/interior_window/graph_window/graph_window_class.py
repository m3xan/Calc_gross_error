# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'graph_window.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QSizePolicy, QToolBar,
    QWidget)

from functions.settings.settings import load_attribute

class Ui_GraphWindow(object):
    def setupUi(self, GraphWindow, user_name):
        if not GraphWindow.objectName():
            GraphWindow.setObjectName(u"GraphWindow")
        GraphWindow.setWindowModality(Qt.ApplicationModal)
        GraphWindow.resize(800, 600)
        GraphWindow.setContextMenuPolicy(Qt.NoContextMenu)
        GraphWindow.setWindowOpacity(0.000000000000000)
        self.action_create_graph = QAction(GraphWindow)
        self.action_create_graph.setObjectName(u"action_create_graph")
        self.action_create_graph.setCheckable(False)
        self.action_create_graph.setEnabled(False)
        self.action_create_graph.setMenuRole(QAction.NoRole)
        self.centralwidget = QWidget(GraphWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        GraphWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QToolBar(GraphWindow)
        self.toolBar.setObjectName(u"toolBar")
        self.toolBar.setContextMenuPolicy(Qt.NoContextMenu)
        self.toolBar.setAllowedAreas(Qt.BottomToolBarArea|Qt.TopToolBarArea)
        self.toolBar.setFloatable(False)
        GraphWindow.addToolBar(eval(load_attribute('window', 'toolBar', user_name)), self.toolBar)

        self.toolBar.addAction(self.action_create_graph)

        self.retranslateUi(GraphWindow)

        QMetaObject.connectSlotsByName(GraphWindow)
    # setupUi

    def retranslateUi(self, GraphWindow):
        GraphWindow.setWindowTitle(QCoreApplication.translate("GraphWindow", u"MainWindow", None))
#if QT_CONFIG(statustip)
        GraphWindow.setStatusTip(QCoreApplication.translate("GraphWindow", u"12312312", None))
#endif // QT_CONFIG(statustip)
        self.action_create_graph.setText(QCoreApplication.translate("GraphWindow", u"\u041f\u043e\u0441\u0442\u0440\u043e\u0438\u0442\u044c \u0433\u0440\u0430\u0444\u0438\u043a", None))
#if QT_CONFIG(shortcut)
        self.action_create_graph.setShortcut(QCoreApplication.translate("GraphWindow", u"Ctrl+K", None))
#endif // QT_CONFIG(shortcut)
        self.toolBar.setWindowTitle(QCoreApplication.translate("GraphWindow", u"toolBar", None))
    # retranslateUi

