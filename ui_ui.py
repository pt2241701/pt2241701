# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QFormLayout, QFrame,
    QGroupBox, QLabel, QMainWindow, QPushButton,
    QRadioButton, QSizePolicy, QStackedWidget, QTabWidget,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1221, 660)
        icon = QIcon()
        icon.addFile(u"icons/france.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: rgb(233, 246, 255)")
        MainWindow.setLocale(QLocale(QLocale.French, QLocale.France))
        MainWindow.setDocumentMode(True)
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.frame_pages = QFrame(self.centralwidget)
        self.frame_pages.setObjectName(u"frame_pages")
        self.frame_pages.setGeometry(QRect(189, 99, 1021, 541))
        self.frame_pages.setMaximumSize(QSize(1021, 541))
        font = QFont()
        font.setBold(True)
        self.frame_pages.setFont(font)
        self.frame_pages.setFrameShape(QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QFrame.Raised)
        self.stackedWidget = QStackedWidget(self.frame_pages)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(-50, 0, 1061, 531))
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        self.stackedWidget.setFont(font1)
        self.stackedWidget.setFrameShape(QFrame.NoFrame)
        self.page_trangchu = QWidget()
        self.page_trangchu.setObjectName(u"page_trangchu")
        self.page_trangchu.setCursor(QCursor(Qt.UpArrowCursor))
        self.page_trangchu.setMouseTracking(False)
        self.page_trangchu.setTabletTracking(False)
        self.page_trangchu.setAcceptDrops(False)
        self.thongtin = QGroupBox(self.page_trangchu)
        self.thongtin.setObjectName(u"thongtin")
        self.thongtin.setGeometry(QRect(40, 20, 1011, 491))
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(True)
        self.thongtin.setFont(font2)
        self.thongtin.setStyleSheet(u"color: black;")
        self.label = QLabel(self.thongtin)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 40, 98, 22))
        self.label.setFont(font2)
        self.label_ten = QLabel(self.thongtin)
        self.label_ten.setObjectName(u"label_ten")
        self.label_ten.setGeometry(QRect(120, 40, 147, 22))
        self.label_ten.setFont(font2)
        self.label_3 = QLabel(self.thongtin)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 100, 110, 22))
        self.label_3.setFont(font2)
        self.label_5 = QLabel(self.thongtin)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 150, 141, 22))
        self.label_5.setFont(font2)
        self.label_6 = QLabel(self.thongtin)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 200, 153, 22))
        self.label_6.setFont(font2)
        self.calendarWidget = QCalendarWidget(self.thongtin)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setGeometry(QRect(10, 230, 376, 221))
        self.calendarWidget.setStyleSheet(u"color: black;\n"
"background-color:white;")
        self.diemnghe = QLabel(self.thongtin)
        self.diemnghe.setObjectName(u"diemnghe")
        self.diemnghe.setGeometry(QRect(140, 100, 55, 21))
        self.diemnghe.setFont(font2)
        self.diemdochieu = QLabel(self.thongtin)
        self.diemdochieu.setObjectName(u"diemdochieu")
        self.diemdochieu.setGeometry(QRect(170, 150, 55, 21))
        self.diemdochieu.setFont(font2)
        self.diemvanpham = QLabel(self.thongtin)
        self.diemvanpham.setObjectName(u"diemvanpham")
        self.diemvanpham.setGeometry(QRect(180, 200, 55, 21))
        self.diemvanpham.setFont(font2)
        self.vebieudo = QPushButton(self.thongtin)
        self.vebieudo.setObjectName(u"vebieudo")
        self.vebieudo.setGeometry(QRect(650, 420, 121, 28))
        self.vebieudo.setFlat(True)
        self.bieudo = QFrame(self.thongtin)
        self.bieudo.setObjectName(u"bieudo")
        self.bieudo.setGeometry(QRect(470, 40, 451, 371))
        self.bieudo.setFrameShape(QFrame.Box)
        self.bieudo.setFrameShadow(QFrame.Raised)
        self.stackedWidget.addWidget(self.page_trangchu)
        self.page_nghe = QWidget()
        self.page_nghe.setObjectName(u"page_nghe")
        self.question_label_nghe = QLabel(self.page_nghe)
        self.question_label_nghe.setObjectName(u"question_label_nghe")
        self.question_label_nghe.setGeometry(QRect(50, 60, 991, 31))
        self.question_label_nghe.setFont(font2)
        self.question_label_nghe.setFrameShape(QFrame.Box)
        self.prev_button = QPushButton(self.page_nghe)
        self.prev_button.setObjectName(u"prev_button")
        self.prev_button.setGeometry(QRect(480, 430, 382, 28))
        font3 = QFont()
        font3.setPointSize(11)
        self.prev_button.setFont(font3)
        icon1 = QIcon()
        icon1.addFile(u"icons/Iconsmind-Outline-Back-2.512.png", QSize(), QIcon.Normal, QIcon.Off)
        self.prev_button.setIcon(icon1)
        self.prev_button.setFlat(True)
        self.play_button = QPushButton(self.page_nghe)
        self.play_button.setObjectName(u"play_button")
        self.play_button.setGeometry(QRect(50, 380, 351, 28))
        self.play_button.setFont(font3)
        icon2 = QIcon()
        icon2.addFile(u"icons/Steve-Zondicons-Play.512.png", QSize(), QIcon.Normal, QIcon.Off)
        self.play_button.setIcon(icon2)
        self.play_button.setFlat(True)
        self.next_button = QPushButton(self.page_nghe)
        self.next_button.setObjectName(u"next_button")
        self.next_button.setGeometry(QRect(480, 380, 382, 28))
        self.next_button.setFont(font3)
        self.next_button.setContextMenuPolicy(Qt.DefaultContextMenu)
        icon3 = QIcon()
        icon3.addFile(u"icons/Iconsmind-Outline-Next-2.512.png", QSize(), QIcon.Normal, QIcon.Off)
        self.next_button.setIcon(icon3)
        self.next_button.setFlat(True)
        self.check_button = QPushButton(self.page_nghe)
        self.check_button.setObjectName(u"check_button")
        self.check_button.setGeometry(QRect(51, 430, 351, 28))
        self.check_button.setFont(font3)
        icon4 = QIcon()
        icon4.addFile(u"icons/Hopstarter-Sleek-Xp-Basic-Ok.256.png", QSize(), QIcon.Normal, QIcon.Off)
        self.check_button.setIcon(icon4)
        self.check_button.setFlat(True)
        self.scorelabelnghe = QLabel(self.page_nghe)
        self.scorelabelnghe.setObjectName(u"scorelabelnghe")
        self.scorelabelnghe.setGeometry(QRect(780, 20, 261, 31))
        font4 = QFont()
        font4.setPointSize(16)
        self.scorelabelnghe.setFont(font4)
        self.scorelabelnghe.setFrameShape(QFrame.Box)
        self.radio_button_1 = QRadioButton(self.page_nghe)
        self.radio_button_1.setObjectName(u"radio_button_1")
        self.radio_button_1.setGeometry(QRect(50, 130, 1001, 31))
        self.radio_button_1.setFont(font)
        self.radio_button_1.setCheckable(True)
        self.radio_button_1.setAutoExclusive(False)
        self.radio_button_3 = QRadioButton(self.page_nghe)
        self.radio_button_3.setObjectName(u"radio_button_3")
        self.radio_button_3.setGeometry(QRect(50, 240, 1001, 31))
        self.radio_button_3.setFont(font)
        self.radio_button_3.setCheckable(True)
        self.radio_button_3.setAutoExclusive(False)
        self.radio_button_2 = QRadioButton(self.page_nghe)
        self.radio_button_2.setObjectName(u"radio_button_2")
        self.radio_button_2.setGeometry(QRect(50, 190, 1001, 31))
        self.radio_button_2.setFont(font)
        self.radio_button_2.setCheckable(True)
        self.radio_button_2.setChecked(False)
        self.radio_button_2.setAutoRepeat(False)
        self.radio_button_2.setAutoExclusive(False)
        self.radio_button_4 = QRadioButton(self.page_nghe)
        self.radio_button_4.setObjectName(u"radio_button_4")
        self.radio_button_4.setGeometry(QRect(50, 300, 1001, 31))
        self.radio_button_4.setFont(font)
        self.radio_button_4.setCheckable(True)
        self.radio_button_4.setAutoRepeat(False)
        self.radio_button_4.setAutoExclusive(False)
        self.switch_file_button = QPushButton(self.page_nghe)
        self.switch_file_button.setObjectName(u"switch_file_button")
        self.switch_file_button.setGeometry(QRect(50, 480, 351, 31))
        font5 = QFont()
        font5.setPointSize(11)
        font5.setBold(False)
        self.switch_file_button.setFont(font5)
        icon5 = QIcon()
        icon5.addFile(u"icons/Treetog-I-Audio-File.256.png", QSize(), QIcon.Normal, QIcon.Off)
        self.switch_file_button.setIcon(icon5)
        self.switch_file_button.setFlat(True)
        self.stackedWidget.addWidget(self.page_nghe)
        self.page_dochieu = QWidget()
        self.page_dochieu.setObjectName(u"page_dochieu")
        self.dochieu_label = QLabel(self.page_dochieu)
        self.dochieu_label.setObjectName(u"dochieu_label")
        self.dochieu_label.setGeometry(QRect(50, 10, 1011, 161))
        font6 = QFont()
        font6.setPointSize(10)
        self.dochieu_label.setFont(font6)
        self.dochieu_label.setFrameShape(QFrame.Box)
        self.question_label_dochieu = QLabel(self.page_dochieu)
        self.question_label_dochieu.setObjectName(u"question_label_dochieu")
        self.question_label_dochieu.setGeometry(QRect(50, 180, 1011, 51))
        self.question_label_dochieu.setFrameShape(QFrame.Box)
        self.question_label_dochieu.setFrameShadow(QFrame.Plain)
        self.answer2_radio_dochieu = QRadioButton(self.page_dochieu)
        self.answer2_radio_dochieu.setObjectName(u"answer2_radio_dochieu")
        self.answer2_radio_dochieu.setGeometry(QRect(50, 290, 1011, 31))
        self.answer3_radio_dochieu = QRadioButton(self.page_dochieu)
        self.answer3_radio_dochieu.setObjectName(u"answer3_radio_dochieu")
        self.answer3_radio_dochieu.setGeometry(QRect(50, 340, 1011, 31))
        self.answer4_radio_dochieu = QRadioButton(self.page_dochieu)
        self.answer4_radio_dochieu.setObjectName(u"answer4_radio_dochieu")
        self.answer4_radio_dochieu.setGeometry(QRect(50, 390, 1001, 31))
        self.answer1_radio_dochieu = QRadioButton(self.page_dochieu)
        self.answer1_radio_dochieu.setObjectName(u"answer1_radio_dochieu")
        self.answer1_radio_dochieu.setEnabled(True)
        self.answer1_radio_dochieu.setGeometry(QRect(50, 240, 1001, 31))
        self.answer1_radio_dochieu.setAutoFillBackground(False)
        self.answer1_radio_dochieu.setInputMethodHints(Qt.ImhNone)
        self.answer1_radio_dochieu.setCheckable(True)
        self.answer1_radio_dochieu.setAutoRepeat(False)
        self.answer1_radio_dochieu.setAutoExclusive(False)
        self.check_button_dochieu = QPushButton(self.page_dochieu)
        self.check_button_dochieu.setObjectName(u"check_button_dochieu")
        self.check_button_dochieu.setGeometry(QRect(50, 440, 441, 41))
        self.check_button_dochieu.setIcon(icon4)
        self.check_button_dochieu.setAutoDefault(False)
        self.check_button_dochieu.setFlat(True)
        self.next_question_button_dochieu = QPushButton(self.page_dochieu)
        self.next_question_button_dochieu.setObjectName(u"next_question_button_dochieu")
        self.next_question_button_dochieu.setEnabled(True)
        self.next_question_button_dochieu.setGeometry(QRect(50, 490, 441, 41))
        self.next_question_button_dochieu.setIcon(icon3)
        self.next_question_button_dochieu.setFlat(True)
        self.next_file_button_dochieu = QPushButton(self.page_dochieu)
        self.next_file_button_dochieu.setObjectName(u"next_file_button_dochieu")
        self.next_file_button_dochieu.setGeometry(QRect(510, 440, 451, 41))
        icon6 = QIcon()
        icon6.addFile(u"icons/Github-Octicons-Arrow-switch-16.512.png", QSize(), QIcon.Normal, QIcon.Off)
        self.next_file_button_dochieu.setIcon(icon6)
        self.next_file_button_dochieu.setFlat(True)
        self.back_question_button_dochieu = QPushButton(self.page_dochieu)
        self.back_question_button_dochieu.setObjectName(u"back_question_button_dochieu")
        self.back_question_button_dochieu.setGeometry(QRect(510, 490, 451, 41))
        self.back_question_button_dochieu.setIcon(icon1)
        self.back_question_button_dochieu.setFlat(True)
        self.scorelabeldochieu = QLabel(self.page_dochieu)
        self.scorelabeldochieu.setObjectName(u"scorelabeldochieu")
        self.scorelabeldochieu.setGeometry(QRect(970, 440, 91, 91))
        font7 = QFont()
        font7.setPointSize(12)
        font7.setBold(True)
        self.scorelabeldochieu.setFont(font7)
        self.scorelabeldochieu.setFrameShape(QFrame.Box)
        self.stackedWidget.addWidget(self.page_dochieu)
        self.page_vanpham = QWidget()
        self.page_vanpham.setObjectName(u"page_vanpham")
        self.scoreLabel = QLabel(self.page_vanpham)
        self.scoreLabel.setObjectName(u"scoreLabel")
        self.scoreLabel.setGeometry(QRect(820, 40, 201, 41))
        self.scoreLabel.setFont(font)
        self.scoreLabel.setFrameShape(QFrame.Box)
        self.questionLabel = QLabel(self.page_vanpham)
        self.questionLabel.setObjectName(u"questionLabel")
        self.questionLabel.setGeometry(QRect(90, 110, 931, 81))
        self.questionLabel.setFont(font)
        self.questionLabel.setStyleSheet(u"color: black;")
        self.questionLabel.setFrameShape(QFrame.Box)
        self.choiceARadioButton = QRadioButton(self.page_vanpham)
        self.choiceARadioButton.setObjectName(u"choiceARadioButton")
        self.choiceARadioButton.setGeometry(QRect(90, 200, 931, 31))
        self.choiceARadioButton.setFont(font)
        self.choiceARadioButton.setStyleSheet(u"color: black;")
        self.choiceARadioButton.setAutoExclusive(False)
        self.choiceBRadioButton = QRadioButton(self.page_vanpham)
        self.choiceBRadioButton.setObjectName(u"choiceBRadioButton")
        self.choiceBRadioButton.setGeometry(QRect(90, 240, 931, 31))
        self.choiceBRadioButton.setFont(font)
        self.choiceBRadioButton.setStyleSheet(u"color: black;")
        self.choiceBRadioButton.setAutoExclusive(False)
        self.choiceDRadioButton = QRadioButton(self.page_vanpham)
        self.choiceDRadioButton.setObjectName(u"choiceDRadioButton")
        self.choiceDRadioButton.setGeometry(QRect(90, 320, 931, 31))
        self.choiceDRadioButton.setFont(font)
        self.choiceDRadioButton.setStyleSheet(u"color: black;")
        self.choiceDRadioButton.setAutoExclusive(False)
        self.choiceCRadioButton = QRadioButton(self.page_vanpham)
        self.choiceCRadioButton.setObjectName(u"choiceCRadioButton")
        self.choiceCRadioButton.setGeometry(QRect(90, 280, 931, 31))
        self.choiceCRadioButton.setFont(font)
        self.choiceCRadioButton.setStyleSheet(u"color: black;")
        self.choiceCRadioButton.setAutoExclusive(False)
        self.answerButton = QPushButton(self.page_vanpham)
        self.answerButton.setObjectName(u"answerButton")
        self.answerButton.setGeometry(QRect(90, 380, 381, 41))
        self.answerButton.setFont(font)
        self.answerButton.setStyleSheet(u"color: black;")
        self.answerButton.setIcon(icon4)
        self.answerButton.setFlat(True)
        self.skipButton = QPushButton(self.page_vanpham)
        self.skipButton.setObjectName(u"skipButton")
        self.skipButton.setGeometry(QRect(90, 430, 381, 41))
        self.skipButton.setFont(font)
        self.skipButton.setStyleSheet(u"color: black;")
        self.skipButton.setIcon(icon3)
        self.skipButton.setFlat(True)
        self.backButton = QPushButton(self.page_vanpham)
        self.backButton.setObjectName(u"backButton")
        self.backButton.setGeometry(QRect(500, 430, 381, 41))
        self.backButton.setFont(font)
        self.backButton.setStyleSheet(u"color: black;")
        self.backButton.setIcon(icon1)
        self.backButton.setFlat(True)
        self.nextButton = QPushButton(self.page_vanpham)
        self.nextButton.setObjectName(u"nextButton")
        self.nextButton.setGeometry(QRect(500, 380, 381, 41))
        self.nextButton.setFont(font)
        self.nextButton.setStyleSheet(u"color: black;")
        self.nextButton.setIcon(icon3)
        self.nextButton.setFlat(True)
        self.stackedWidget.addWidget(self.page_vanpham)
        self.left_side_menu = QFrame(self.centralwidget)
        self.left_side_menu.setObjectName(u"left_side_menu")
        self.left_side_menu.setGeometry(QRect(20, 90, 50, 531))
        self.left_side_menu.setMaximumSize(QSize(50, 16777215))
        self.left_side_menu.setFont(font)
        self.left_side_menu.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(233, 246, 255)\n"
"}\n"
"QPushButton{\n"
"	padding: 20px 10px;\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"	background-color: #fff;\n"
"	color: #fff;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #fff;\n"
"}")
        self.left_side_menu.setFrameShape(QFrame.NoFrame)
        self.left_side_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.left_side_menu)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(7, 0, 0, 0)
        self.left_menu_top_buttons = QFrame(self.left_side_menu)
        self.left_menu_top_buttons.setObjectName(u"left_menu_top_buttons")
        self.left_menu_top_buttons.setFont(font)
        self.left_menu_top_buttons.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(233, 246, 255)\n"
"}\n"
"QPushButton{\n"
"	padding: 20px 10px;\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"	background-color: #fff;\n"
"	color: #000;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(0,92,157);\n"
"}")
        self.left_menu_top_buttons.setFrameShape(QFrame.StyledPanel)
        self.left_menu_top_buttons.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.left_menu_top_buttons)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(0)
        self.formLayout.setVerticalSpacing(0)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.trangchu = QPushButton(self.left_menu_top_buttons)
        self.trangchu.setObjectName(u"trangchu")
        self.trangchu.setMinimumSize(QSize(100, 0))
        self.trangchu.setFont(font)
        self.trangchu.setStyleSheet(u"background-image:url(:/icons/icons/home.svg);\n"
"background-repeat : none;\n"
"background-position : center left;\n"
"color: black;\n"
"padding-left : 40px;\n"
"background-color: rgb(233, 246, 255)")
        icon7 = QIcon()
        icon7.addFile(u"icons/Custom-Icon-Design-Mono-General-3-Home.512.png", QSize(), QIcon.Normal, QIcon.Off)
        self.trangchu.setIcon(icon7)
        self.trangchu.setAutoDefault(False)
        self.trangchu.setFlat(True)

        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.trangchu)

        self.dochieu = QPushButton(self.left_menu_top_buttons)
        self.dochieu.setObjectName(u"dochieu")
        self.dochieu.setMinimumSize(QSize(100, 0))
        self.dochieu.setFont(font)
        self.dochieu.setStyleSheet(u"background-image:url(:/icons/icons/pen-tool.svg);\n"
"background-repeat : none;\n"
"background-position : center left;\n"
"color: black;\n"
"padding-left : 25px;\n"
"background-color: rgb(233, 246, 255)")
        icon8 = QIcon()
        icon8.addFile(u"icons/Icons8-Windows-8-Science-Literature.512.png", QSize(), QIcon.Normal, QIcon.Off)
        self.dochieu.setIcon(icon8)
        self.dochieu.setFlat(True)

        self.formLayout.setWidget(2, QFormLayout.SpanningRole, self.dochieu)

        self.vanpham = QPushButton(self.left_menu_top_buttons)
        self.vanpham.setObjectName(u"vanpham")
        self.vanpham.setMinimumSize(QSize(100, 0))
        self.vanpham.setFont(font)
        self.vanpham.setStyleSheet(u"background-image:url(:/icons/icons/book-open.svg);\n"
"background-repeat : none;\n"
"background-position : center left;\n"
"color: black;\n"
"padding-left : 31px;\n"
"background-color: rgb(233, 246, 255)")
        icon9 = QIcon()
        icon9.addFile(u"icons/Designcontest-Outline-Pencil.256.png", QSize(), QIcon.Normal, QIcon.Off)
        self.vanpham.setIcon(icon9)
        self.vanpham.setFlat(True)

        self.formLayout.setWidget(3, QFormLayout.SpanningRole, self.vanpham)

        self.nghe = QPushButton(self.left_menu_top_buttons)
        self.nghe.setObjectName(u"nghe")
        self.nghe.setMinimumSize(QSize(100, 0))
        self.nghe.setFont(font)
        self.nghe.setStyleSheet(u"background-image:url(:/icons/icons/headphones.svg);\n"
"background-repeat : none;\n"
"background-position : center left;\n"
"color: black;\n"
"padding-left : 4px;\n"
"background-color: rgb(233, 246, 255)")
        icon10 = QIcon()
        icon10.addFile(u"icons/Steve-Zondicons-Headphones.512.png", QSize(), QIcon.Normal, QIcon.Off)
        self.nghe.setIcon(icon10)
        self.nghe.setFlat(True)

        self.formLayout.setWidget(1, QFormLayout.SpanningRole, self.nghe)


        self.verticalLayout_2.addWidget(self.left_menu_top_buttons)

        self.exit_button = QPushButton(self.left_side_menu)
        self.exit_button.setObjectName(u"exit_button")
        self.exit_button.setMinimumSize(QSize(100, 0))
        self.exit_button.setFont(font)
        self.exit_button.setStyleSheet(u"background-image:url(:/icons/icons/arrow-left-circle.svg);\n"
"background-repeat : none;\n"
"background-position : center left;\n"
"color: black;\n"
"padding-left : 2px;\n"
"background-color: rgb(233, 246, 255)")
        icon11 = QIcon()
        icon11.addFile(u"icons/Aniket-Suvarna-Box-Regular-Bx-log-out.512.png", QSize(), QIcon.Normal, QIcon.Off)
        self.exit_button.setIcon(icon11)
        self.exit_button.setFlat(True)

        self.verticalLayout_2.addWidget(self.exit_button)

        self.header = QFrame(self.centralwidget)
        self.header.setObjectName(u"header")
        self.header.setGeometry(QRect(10, 0, 1201, 91))
        self.header.setFont(font)
        self.header.setFrameShape(QFrame.StyledPanel)
        self.header.setFrameShadow(QFrame.Raised)
        self.francaisestlavie = QLabel(self.header)
        self.francaisestlavie.setObjectName(u"francaisestlavie")
        self.francaisestlavie.setGeometry(QRect(440, 20, 351, 35))
        font8 = QFont()
        font8.setFamilies([u"MS Serif"])
        font8.setPointSize(26)
        font8.setBold(True)
        font8.setItalic(False)
        font8.setUnderline(False)
        font8.setStrikeOut(False)
        font8.setKerning(True)
        self.francaisestlavie.setFont(font8)
        self.francaisestlavie.setLayoutDirection(Qt.LeftToRight)
        self.francaisestlavie.setAutoFillBackground(False)
        self.francaisestlavie.setStyleSheet(u"color: black;")
        self.menuBtn = QPushButton(self.header)
        self.menuBtn.setObjectName(u"menuBtn")
        self.menuBtn.setGeometry(QRect(20, 30, 50, 51))
        self.menuBtn.setMinimumSize(QSize(50, 0))
        self.menuBtn.setMaximumSize(QSize(50, 16777215))
        self.menuBtn.setFont(font)
        icon12 = QIcon()
        icon12.addFile(u"icons/Icons8-Windows-8-Very-Basic-Menu.512.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menuBtn.setIcon(icon12)
        self.menuBtn.setFlat(False)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)
        self.vebieudo.setDefault(True)
        self.prev_button.setDefault(True)
        self.play_button.setDefault(True)
        self.next_button.setDefault(True)
        self.check_button.setDefault(True)
        self.switch_file_button.setDefault(True)
        self.check_button_dochieu.setDefault(True)
        self.next_question_button_dochieu.setDefault(True)
        self.next_file_button_dochieu.setDefault(True)
        self.back_question_button_dochieu.setDefault(True)
        self.answerButton.setDefault(True)
        self.skipButton.setDefault(True)
        self.backButton.setDefault(True)
        self.nextButton.setDefault(True)
        self.trangchu.setDefault(True)
        self.dochieu.setDefault(True)
        self.vanpham.setDefault(True)
        self.nghe.setDefault(True)
        self.exit_button.setDefault(True)
        self.menuBtn.setDefault(True)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"FranceEstLaVie", None))
        self.thongtin.setTitle(QCoreApplication.translate("MainWindow", u"TH\u00d4NG TIN H\u1eccC VI\u00caN", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"H\u1ecd v\u00e0 t\u00ean: ", None))
        self.label_ten.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0110i\u1ec3m nghe: ", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0110i\u1ec3m \u0111\u1ecdc hi\u1ec3u: ", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0110i\u1ec3m v\u0103n ph\u1ea1m: ", None))
        self.diemnghe.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.diemdochieu.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.diemvanpham.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.vebieudo.setText(QCoreApplication.translate("MainWindow", u"BI\u1ec2U \u0110\u1ed2 \u0110I\u1ec2M S\u1ed0: ", None))
        self.question_label_nghe.setText(QCoreApplication.translate("MainWindow", u"Question:", None))
        self.prev_button.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.play_button.setText(QCoreApplication.translate("MainWindow", u"Play", None))
        self.next_button.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.check_button.setText(QCoreApplication.translate("MainWindow", u"Check", None))
        self.scorelabelnghe.setText("")
        self.radio_button_1.setText("")
        self.radio_button_3.setText("")
        self.radio_button_2.setText("")
        self.radio_button_4.setText("")
        self.switch_file_button.setText(QCoreApplication.translate("MainWindow", u"Qua b\u00e0i m\u1edbi", None))
        self.check_button_dochieu.setText(QCoreApplication.translate("MainWindow", u"Ki\u1ec3m tra", None))
        self.next_question_button_dochieu.setText(QCoreApplication.translate("MainWindow", u"C\u00e2u h\u1ecfi ti\u1ebfp theo", None))
        self.next_file_button_dochieu.setText(QCoreApplication.translate("MainWindow", u"File ti\u1ebfp theo", None))
        self.back_question_button_dochieu.setText(QCoreApplication.translate("MainWindow", u"Quay lai", None))
        self.scorelabeldochieu.setText("")
        self.scoreLabel.setText("")
        self.questionLabel.setText("")
        self.answerButton.setText(QCoreApplication.translate("MainWindow", u"Tr\u1ea3 l\u1eddi", None))
        self.skipButton.setText(QCoreApplication.translate("MainWindow", u"B\u1ecf qua", None))
        self.backButton.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.nextButton.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.trangchu.setText(QCoreApplication.translate("MainWindow", u"TRANG CH\u1ee6", None))
        self.dochieu.setText(QCoreApplication.translate("MainWindow", u"\u0110\u1eccC HI\u1ec2U", None))
        self.vanpham.setText(QCoreApplication.translate("MainWindow", u"V\u0102N PH\u1ea0M", None))
        self.nghe.setText(QCoreApplication.translate("MainWindow", u"NGHE", None))
        self.exit_button.setText(QCoreApplication.translate("MainWindow", u"EXIT", None))
        self.francaisestlavie.setText(QCoreApplication.translate("MainWindow", u"FRANCAIS EST LA VIE", None))
        self.menuBtn.setText(QCoreApplication.translate("MainWindow", u"MENU", None))
    # retranslateUi

