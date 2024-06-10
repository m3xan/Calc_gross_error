# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'auto_save.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QCheckBox, QDialog,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QSpinBox, QVBoxLayout, QWidget)
from window.main_window import res_rc

class Ui_DialogAutoSave(object):
    def setupUi(self, DialogAutoSave):
        if not DialogAutoSave.objectName():
            DialogAutoSave.setObjectName(u"DialogAutoSave")
        DialogAutoSave.resize(272, 139)
        icon = QIcon()
        icon.addFile(u":/icon/calculator-Freepik.png", QSize(), QIcon.Normal, QIcon.Off)
        DialogAutoSave.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(DialogAutoSave)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.check_box_auto_save = QCheckBox(DialogAutoSave)
        self.check_box_auto_save.setObjectName(u"check_box_auto_save")
        self.check_box_auto_save.setFocusPolicy(Qt.NoFocus)
        self.check_box_auto_save.setContextMenuPolicy(Qt.NoContextMenu)
        self.check_box_auto_save.setInputMethodHints(Qt.ImhTime)
        self.check_box_auto_save.setChecked(False)
        self.check_box_auto_save.setAutoRepeat(False)
        self.check_box_auto_save.setAutoExclusive(False)
        self.check_box_auto_save.setTristate(False)

        self.horizontalLayout_2.addWidget(self.check_box_auto_save)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(DialogAutoSave)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.spinBox = QSpinBox(DialogAutoSave)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setWrapping(False)
        self.spinBox.setReadOnly(False)
        self.spinBox.setProperty("showGroupSeparator", True)
        self.spinBox.setMinimum(2)
        self.spinBox.setStepType(QAbstractSpinBox.AdaptiveDecimalStepType)

        self.horizontalLayout.addWidget(self.spinBox)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.check_box_save_user_name = QCheckBox(DialogAutoSave)
        self.check_box_save_user_name.setObjectName(u"check_box_save_user_name")

        self.verticalLayout_2.addWidget(self.check_box_save_user_name)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_window_size = QLabel(DialogAutoSave)
        self.label_window_size.setObjectName(u"label_window_size")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_window_size.sizePolicy().hasHeightForWidth())
        self.label_window_size.setSizePolicy(sizePolicy)

        self.horizontalLayout_4.addWidget(self.label_window_size)

        self.spin_box_window_size = QSpinBox(DialogAutoSave)
        self.spin_box_window_size.setObjectName(u"spin_box_window_size")
        self.spin_box_window_size.setWrapping(False)
        self.spin_box_window_size.setReadOnly(False)
        self.spin_box_window_size.setProperty("showGroupSeparator", True)
        self.spin_box_window_size.setMinimum(4)
        self.spin_box_window_size.setMaximum(10)
        self.spin_box_window_size.setStepType(QAbstractSpinBox.AdaptiveDecimalStepType)

        self.horizontalLayout_4.addWidget(self.spin_box_window_size)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)


        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.push_button_save = QPushButton(DialogAutoSave)
        self.push_button_save.setObjectName(u"push_button_save")

        self.horizontalLayout_3.addWidget(self.push_button_save)

        self.push_button_esc = QPushButton(DialogAutoSave)
        self.push_button_esc.setObjectName(u"push_button_esc")

        self.horizontalLayout_3.addWidget(self.push_button_esc)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.retranslateUi(DialogAutoSave)

        QMetaObject.connectSlotsByName(DialogAutoSave)
    # setupUi

    def retranslateUi(self, DialogAutoSave):
        DialogAutoSave.setWindowTitle(QCoreApplication.translate("DialogAutoSave", u"\u0410\u0432\u0442\u043e \u0441\u043e\u0445\u0440\u043e\u043d\u0435\u043d\u0438\u0435", None))
        self.check_box_auto_save.setText(QCoreApplication.translate("DialogAutoSave", u"\u0410\u0432\u0442\u043e\u0441\u043e\u0445\u0440\u043e\u043d\u0435\u043d\u0438\u0435", None))
        self.label.setText(QCoreApplication.translate("DialogAutoSave", u"\u0410\u0432\u0442\u043e\u0441\u043e\u0445\u0440\u043e\u043d\u0435\u043d\u0438\u0435 \u0447\u0435\u0440\u0435\u0437 \u043a\u0430\u0436\u0434\u044b\u0435(\u043c\u0438\u043d\u0443\u0442)", None))
        self.check_box_save_user_name.setText(QCoreApplication.translate("DialogAutoSave", u"\u0417\u0430\u043f\u043e\u043c\u043d\u0438\u0442\u044c \u043c\u0435\u043d\u044f", None))
        self.label_window_size.setText(QCoreApplication.translate("DialogAutoSave", u"\u041e\u043a\u043d\u043e \u0434\u043b\u044f \u0443\u0441\u0440\u0435\u0434\u043d\u0435\u043d\u0438\u044f", None))
        self.push_button_save.setText(QCoreApplication.translate("DialogAutoSave", u"\u0421\u043e\u0445\u0440\u043e\u043d\u0438\u0442\u044c ", None))
        self.push_button_esc.setText(QCoreApplication.translate("DialogAutoSave", u"\u0412\u044b\u0439\u0442\u0438", None))
    # retranslateUi

