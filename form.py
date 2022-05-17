# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLayout, QProgressBar,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.ApplicationModal)
        MainWindow.resize(1366, 728)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u"gh.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(True)
        self.verticalLayout = QVBoxLayout(MainWindow)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetMaximumSize)
        self.verticalLayout.setContentsMargins(0, 0, 0, 3)
        self.frame_2 = QFrame(MainWindow)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.frame_2)

        self.frame = QFrame(MainWindow)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(100, 50))
        self.frame.setMaximumSize(QSize(12321312, 60))
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.WinPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(8, 0, 0, 2)
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(200, 80))
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(7)
        self.gridLayout.setVerticalSpacing(1)
        self.gridLayout.setContentsMargins(0, 0, 0, 6)
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setPointSize(10)
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(92, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 1, 1, 2)

        self.comboBox = QComboBox(self.frame_3)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(0, 30))
        self.comboBox.setMaximumSize(QSize(16777215, 30))
        self.comboBox.setStyleSheet(u"QComboBox {\n"
"     border: 1px solid gray;\n"
"     border-radius: 3px;\n"
"     padding: 1px 18px 1px 3px;\n"
" }\n"
"\n"
" QComboBox:editable {\n"
"     background: white;\n"
" }")

        self.gridLayout.addWidget(self.comboBox, 1, 0, 1, 2)

        self.pushButton_2 = QPushButton(self.frame_3)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u" QPushButton {\n"
"	background-color: rgb(245, 255, 226);\n"
"     border-style: outset;\n"
"     border-width: 0.5px;\n"
"     border-radius: 8px;\n"
"     border-color: black;\n"
"     font:12px;\n"
"     padding: 6px;\n"
" }\n"
" QPushButton:pressed {\n"
"	background-color: rgb(170, 170, 255);\n"
"     border-style: inset;\n"
" }\n"
"\n"
" QPushButton:indicator:checked {\n"
"	\n"
"	background-color: rgb(124, 137, 255);\n"
"     border-style: inset;\n"
" }")

        self.gridLayout.addWidget(self.pushButton_2, 1, 2, 1, 1)


        self.horizontalLayout.addWidget(self.frame_3)

        self.horizontalSpacer_3 = QSpacerItem(100, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(100, 30))
        self.pushButton.setMaximumSize(QSize(16777215, 48))
        self.pushButton.setStyleSheet(u" QPushButton {\n"
"	background-color: rgb(245, 255, 226);\n"
"     border-style: outset;\n"
"     border-width: 0.5px;\n"
"     border-radius: 8px;\n"
"     border-color: black;\n"
"     font:18px;\n"
"     padding: 6px;\n"
" }\n"
" QPushButton:pressed {\n"
"	background-color: rgb(170, 170, 255);\n"
"     border-style: inset;\n"
" }\n"
"\n"
" QPushButton:indicator:checked {\n"
"	\n"
"	background-color: rgb(124, 137, 255);\n"
"     border-style: inset;\n"
" }")
        self.pushButton.setCheckable(False)
        self.pushButton.setChecked(False)

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton2 = QPushButton(self.frame)
        self.pushButton2.setObjectName(u"pushButton2")
        self.pushButton2.setMinimumSize(QSize(100, 30))
        self.pushButton2.setMaximumSize(QSize(16777215, 48))
        self.pushButton2.setStyleSheet(u" QPushButton {\n"
"	background-color: rgb(245, 255, 226);\n"
"     border-style: outset;\n"
"     border-width: 0.5px;\n"
"     border-radius: 8px;\n"
"     border-color: black;\n"
"     font:18px;\n"
"     padding: 6px;\n"
" }\n"
" QPushButton:pressed {\n"
"	background-color: rgb(170, 170, 255);\n"
"     border-style: inset;\n"
" }\n"
"\n"
" QPushButton:indicator:checked {\n"
"	\n"
"	background-color: rgb(124, 137, 255);\n"
"     border-style: inset;\n"
" }")

        self.horizontalLayout.addWidget(self.pushButton2)

        self.pushButton3 = QPushButton(self.frame)
        self.pushButton3.setObjectName(u"pushButton3")
        self.pushButton3.setMinimumSize(QSize(156, 40))
        self.pushButton3.setMaximumSize(QSize(16777215, 48))
        self.pushButton3.setStyleSheet(u" QPushButton {\n"
"background-color: rgb(245, 255, 226);\n"
"     border-style: outset;\n"
"     border-width: 0.5px;\n"
"     border-radius: 8px;\n"
"     border-color: black;\n"
"     font:14px;\n"
"     padding: 6px;\n"
" }\n"
" QPushButton:pressed {\n"
"	background-color: rgb(170, 170, 255);\n"
"     border-style: inset;\n"
" }\n"
"\n"
" QPushButton:indicator:checked {\n"
"	\n"
"	background-color: rgb(124, 137, 255);\n"
"     border-style: inset;\n"
" }")

        self.horizontalLayout.addWidget(self.pushButton3)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(200, 16777215))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 0, 0, 11)
        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.progressBar = QProgressBar(self.frame_4)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMaximumSize(QSize(200, 16777215))
        self.progressBar.setValue(0)

        self.verticalLayout_2.addWidget(self.progressBar)


        self.horizontalLayout.addWidget(self.frame_4)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"STM32", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0440\u0442:", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0443\u0441\u043a", None))
        self.pushButton2.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043b\u0438\u0431\u0440\u043e\u0432\u043a\u0430", None))
        self.pushButton3.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0443\u0441\u043a \n"
"\u0441 \u043a\u0430\u043b\u0438\u0431\u0440\u043e\u0432\u043a\u043e\u0439", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u043a\u0430:", None))
    # retranslateUi

