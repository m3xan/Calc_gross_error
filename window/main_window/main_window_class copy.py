# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDockWidget, QFrame,
    QHBoxLayout, QLayout, QListWidget, QListWidgetItem,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)


from settings.settings import load_setting_window

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(839, 572)
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setContextMenuPolicy(Qt.NoContextMenu)
        icon = QIcon()
        icon.addFile(u":/calculator-Freepik.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setInputMethodHints(Qt.ImhNone)
        self.action_info = QAction(MainWindow)
        self.action_info.setObjectName(u"action_info")
        self.action_info.setCheckable(False)
        icon1 = QIcon()
        icon1.addFile(u":/info.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_info.setIcon(icon1)
        self.action_save = QAction(MainWindow)
        self.action_save.setObjectName(u"action_save")
        self.action_save.setCheckable(True)
        self.action_save.setEnabled(True)
        icon2 = QIcon()
        iconThemeName = u"document-new"
        if QIcon.hasThemeIcon(iconThemeName):
            icon2 = QIcon.fromTheme(iconThemeName)
        else:
            icon2.addFile(u":/save.png", QSize(), QIcon.Normal, QIcon.Off)

        self.action_save.setIcon(icon2)
        self.action_esc = QAction(MainWindow)
        self.action_esc.setObjectName(u"action_esc")
        icon3 = QIcon()
        icon3.addFile(u":/leave.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_esc.setIcon(icon3)
        self.action_excel = QAction(MainWindow)
        self.action_excel.setObjectName(u"action_excel")
        icon4 = QIcon()
        iconThemeName = u"accessories-calculator"
        if QIcon.hasThemeIcon(iconThemeName):
            icon4 = QIcon.fromTheme(iconThemeName)
        else:
            icon4.addFile(u":/exel.png", QSize(), QIcon.Normal, QIcon.Off)

        self.action_excel.setIcon(icon4)
        self.action_bd = QAction(MainWindow)
        self.action_bd.setObjectName(u"action_bd")
        icon5 = QIcon()
        icon5.addFile(u":/bd.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.action_bd.setIcon(icon5)
        self.action_help = QAction(MainWindow)
        self.action_help.setObjectName(u"action_help")
        icon6 = QIcon()
        iconThemeName = u"accessories-calculator"
        if QIcon.hasThemeIcon(iconThemeName):
            icon6 = QIcon.fromTheme(iconThemeName)
        else:
            icon6.addFile(u":/-help-outline_89965.ico", QSize(), QIcon.Normal, QIcon.Off)

        self.action_help.setIcon(icon6)
        self.action_save_as = QAction(MainWindow)
        self.action_save_as.setObjectName(u"action_save_as")
        icon7 = QIcon()
        icon7.addFile(u":/save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_save_as.setIcon(icon7)
        self.action_new = QAction(MainWindow)
        self.action_new.setObjectName(u"action_new")
        icon8 = QIcon()
        icon8.addFile(u":/plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_new.setIcon(icon8)
        self.action_setting_window = QAction(MainWindow)
        self.action_setting_window.setObjectName(u"action_setting_window")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.horizontalLayout.setContentsMargins(9, -1, 6, -1)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(500, 500))
        self.frame.setContextMenuPolicy(Qt.NoContextMenu)
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.frame)

        self.push_button_create_graph = QPushButton(self.centralwidget)
        self.push_button_create_graph.setObjectName(u"push_button_create_graph")
        self.push_button_create_graph.setEnabled(True)

        self.verticalLayout_2.addWidget(self.push_button_create_graph)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 839, 22))
        self.menubar.setContextMenuPolicy(Qt.NoContextMenu)
        self.menubar.setDefaultUp(False)
        self.menubar.setNativeMenuBar(True)
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        self.menu_3 = QMenu(self.menubar)
        self.menu_3.setObjectName(u"menu_3")
        self.menu_4 = QMenu(self.menu_3)
        self.menu_4.setObjectName(u"menu_4")
        icon9 = QIcon()
        icon9.addFile(u":/file.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_4.setIcon(icon9)
        self.menu_5 = QMenu(self.menubar)
        self.menu_5.setObjectName(u"menu_5")
        MainWindow.setMenuBar(self.menubar)
        self.dockWidget = QDockWidget(MainWindow)
        self.dockWidget.setObjectName(u"dockWidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.dockWidget.sizePolicy().hasHeightForWidth())
        self.dockWidget.setSizePolicy(sizePolicy2)
        self.dockWidget.setMinimumSize(QSize(318, 500))
        self.dockWidget.setMaximumSize(QSize(400, 524287))
        self.dockWidget.setFeatures(QDockWidget.DockWidgetFloatable|QDockWidget.DockWidgetMovable)
        self.dockWidget.setAllowedAreas(Qt.LeftDockWidgetArea|Qt.RightDockWidgetArea)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.dockWidgetContents.setLayoutDirection(Qt.LeftToRight)
        self.dockWidgetContents.setAutoFillBackground(False)
        self.verticalLayout = QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(6, 3, 6, 9)
        self.combo_box_selection_data = QComboBox(self.dockWidgetContents)
        self.combo_box_selection_data.setObjectName(u"combo_box_selection_data")
        self.combo_box_selection_data.setEnabled(True)
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(150)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.combo_box_selection_data.sizePolicy().hasHeightForWidth())
        self.combo_box_selection_data.setSizePolicy(sizePolicy3)
        self.combo_box_selection_data.setMinimumSize(QSize(300, 0))
        self.combo_box_selection_data.setMaximumSize(QSize(400, 16777215))

        self.verticalLayout.addWidget(self.combo_box_selection_data)

        self.combo_box_selection_metod = QComboBox(self.dockWidgetContents)
        self.combo_box_selection_metod.setObjectName(u"combo_box_selection_metod")
        self.combo_box_selection_metod.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.combo_box_selection_metod.sizePolicy().hasHeightForWidth())
        self.combo_box_selection_metod.setSizePolicy(sizePolicy3)
        self.combo_box_selection_metod.setMinimumSize(QSize(300, 0))
        self.combo_box_selection_metod.setMaximumSize(QSize(400, 16777215))

        self.verticalLayout.addWidget(self.combo_box_selection_metod)

        self.listWidget = QListWidget(self.dockWidgetContents)
        self.listWidget.setObjectName(u"listWidget")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy4)
        self.listWidget.setMinimumSize(QSize(300, 0))
        self.listWidget.setMaximumSize(QSize(400, 16777215))
        self.listWidget.setContextMenuPolicy(Qt.CustomContextMenu)

        self.verticalLayout.addWidget(self.listWidget)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(7)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SetFixedSize)
        self.horizontalLayout_3.setContentsMargins(0, -1, 0, -1)
        self.push_button_add_data = QPushButton(self.dockWidgetContents)
        self.push_button_add_data.setObjectName(u"push_button_add_data")
        self.push_button_add_data.setMinimumSize(QSize(0, 0))
        self.push_button_add_data.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_3.addWidget(self.push_button_add_data)

        self.push_button_delite_data = QPushButton(self.dockWidgetContents)
        self.push_button_delite_data.setObjectName(u"push_button_delite_data")
        self.push_button_delite_data.setMinimumSize(QSize(0, 0))
        self.push_button_delite_data.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_3.addWidget(self.push_button_delite_data)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.push_button_create_calc = QPushButton(self.dockWidgetContents)
        self.push_button_create_calc.setObjectName(u"push_button_create_calc")
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.push_button_create_calc.sizePolicy().hasHeightForWidth())
        self.push_button_create_calc.setSizePolicy(sizePolicy5)
        self.push_button_create_calc.setMinimumSize(QSize(300, 0))
        self.push_button_create_calc.setMaximumSize(QSize(400, 16777215))

        self.verticalLayout.addWidget(self.push_button_create_calc)

        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(eval(load_setting_window("dockWidget")), self.dockWidget)
        self.dockWidget.raise_()

        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_5.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.menu.addSeparator()
        self.menu.addAction(self.action_info)
        self.menu_2.addAction(self.action_help)
        self.menu_3.addAction(self.action_new)
        self.menu_3.addAction(self.menu_4.menuAction())
        self.menu_3.addAction(self.action_save)
        self.menu_3.addAction(self.action_save_as)
        self.menu_3.addSeparator()
        self.menu_3.addAction(self.action_esc)
        self.menu_4.addAction(self.action_excel)
        self.menu_4.addAction(self.action_bd)
        self.menu_5.addAction(self.action_setting_window)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0430 \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u043e\u0432", None))
        self.action_info.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f", None))
#if QT_CONFIG(shortcut)
        self.action_info.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+.", None))
#endif // QT_CONFIG(shortcut)
        self.action_save.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c ", None))
#if QT_CONFIG(shortcut)
        self.action_save.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.action_esc.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0439\u0442\u0438", None))
        self.action_excel.setText(QCoreApplication.translate("MainWindow", u"Excel", None))
#if QT_CONFIG(shortcut)
        self.action_excel.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+1", None))
#endif // QT_CONFIG(shortcut)
        self.action_bd.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0414", None))
#if QT_CONFIG(shortcut)
        self.action_bd.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+2", None))
#endif // QT_CONFIG(shortcut)
        self.action_help.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f", None))
        self.action_save_as.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u043a\u0430\u043a", None))
#if QT_CONFIG(shortcut)
        self.action_save_as.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+S", None))
#endif // QT_CONFIG(shortcut)
        self.action_new.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u0430\u044f \u0437\u0430\u043f\u0438\u0441\u044c", None))
        self.action_setting_window.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0442\u0435\u0440\u0444\u0435\u0439\u0441", None))
        self.push_button_create_graph.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u0442\u0440\u043e\u0438\u0442\u044c \u0433\u0440\u0430\u0444\u0438\u043a", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u041e \u043d\u0430\u0441", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043c\u043e\u0449\u044c", None))
        self.menu_3.setTitle(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b", None))
        self.menu_4.setTitle(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c", None))
        self.menu_5.setTitle(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.dockWidget.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041b\u0438\u0441\u0442 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0439", None))
        self.push_button_add_data.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.push_button_delite_data.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.push_button_create_calc.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0447\u0438\u0442\u0430\u0442\u044c", None))
    # retranslateUi

