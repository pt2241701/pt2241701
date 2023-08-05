# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dochieu.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_QuizApp(object):
    def setupUi(self, QuizApp):
        if not QuizApp.objectName():
            QuizApp.setObjectName(u"QuizApp")
        QuizApp.resize(734, 472)
        self.centralwidget = QWidget(QuizApp)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        QuizApp.setCentralWidget(self.centralwidget)

        self.retranslateUi(QuizApp)

        QMetaObject.connectSlotsByName(QuizApp)
    # setupUi

    def retranslateUi(self, QuizApp):
        QuizApp.setWindowTitle(QCoreApplication.translate("QuizApp", u"Quiz App", None))
    # retranslateUi

