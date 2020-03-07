# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
from time import strftime
import datetime
from PyQt5.QtGui import QIcon


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 640)
        MainWindow.setStyleSheet("background-color :rgb(44, 86, 151)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(10, 10, 461, 171))
        self.logo.setObjectName("logo")
        self.Head = QtWidgets.QLabel(self.centralwidget)
        self.Head.setGeometry(QtCore.QRect(0, 240, 481, 91))
        self.Head.setObjectName("Head")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(92, 350, 201, 31))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        validator = QtGui.QIntValidator()
        self.lineEdit.setValidator(validator)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(300, 350, 101, 31))
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet("""

            QPushButton:!hover { font-weight:490; background-color: white }
            QPushButton:hover { font-weight:490; color: rgb(255, 255, 255) ;background-color: rgb(44, 86, 151) }
            QPushButton:pressed { font-weight:490; color: rgb(255, 255, 255); background-color: rgb(44, 86, 151); }
        """)
        self.pushButton.clicked.connect(self.send_id)
        self.error = QtWidgets.QLabel(self.centralwidget)
        self.error.setGeometry(QtCore.QRect(90, 390, 281, 20))
        self.error.setObjectName("error")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)





    def send_id(self):
        data = ['000000','010203','030609']
        global id
        id = self.lineEdit.text()
        if id in data:
            ctg = QtWidgets.QDialog()
            ui8 = Ui_ctg()
            ui8.setupUi(ctg)
            ctg.show()
            ctg.exec()
        else:
            self.error.setText(
                "<html><head/><body><p><span style=\" font-weight:600; color:#ffffff;\">Сотрудника с таким номером не существует!</span></p></body></html>")


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "NLMK Control"))
        self.Head.setText(_translate("MainWindow",
                                     "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; color:#ffffff;\">Добро пожаловать в СКК НЛМК</span></p><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">Пожалуйста, укажите номер Вашего бейджа</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Отправить"))
        self.logo.setText(_translate("ctg",
                                     "<html><head/><body><p align=\"center\"><img src=\":/newPrefix/nlmk_belyy_png (1).png\"/></p></body></html>"))

class Ui_ctg(object):
    def setupUi(self, ctg):
        ctg.setObjectName("ctg")
        ctg.resize(480, 640)
        ctg.setStyleSheet("background-color: rgb(44, 86, 151);")
        self.text_select = QtWidgets.QLabel(ctg)
        self.text_select.setGeometry(QtCore.QRect(10, 210, 451, 31))
        self.text_select.setStyleSheet("font: 14pt \"Circe\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.text_select.setObjectName("text_select")
        self.ctgr1 = QtWidgets.QPushButton(ctg)
        self.ctgr1.setGeometry(QtCore.QRect(140, 260, 211, 41))
        self.ctgr1.setStyleSheet("""

            QPushButton:!hover { font-weight:490; background-color: white }
            QPushButton:hover { font-weight:490; color: rgb(255, 255, 255) ;background-color: rgb(44, 86, 151) }
            QPushButton:pressed { font-weight:490; color: rgb(255, 255, 255); background-color: rgb(44, 86, 151); }
        """)
        self.ctgr1.setObjectName("ctgr1")
        self.ctgr1.clicked.connect(self.ctgr_one_clicked)
        self.ctgr2 = QtWidgets.QPushButton(ctg)
        self.ctgr2.setGeometry(QtCore.QRect(140, 320, 211, 41))
        self.ctgr2.setStyleSheet("""

            QPushButton:!hover { font-weight:490 ; background-color: white }
            QPushButton:hover { font-weight:490 ; color: rgb(255, 255, 255) ;background-color: rgb(44, 86, 151) }
            QPushButton:pressed { font-weight:490 ; color: rgb(255, 255, 255); background-color: rgb(44, 86, 151); }
        """)
        self.ctgr2.setObjectName("ctgr2")
        self.ctgr2.clicked.connect(self.ctgr_two_clicked)
        self.ctgr3 = QtWidgets.QPushButton(ctg)
        self.ctgr3.setGeometry(QtCore.QRect(140, 380, 211, 41))
        self.ctgr3.setStyleSheet("""

            QPushButton:!hover { font-weight:490; background-color: white }
            QPushButton:hover { font-weight:490; color: rgb(255, 255, 255) ;background-color: rgb(44, 86, 151) }
            QPushButton:pressed { font-weight:490; color: rgb(255, 255, 255); background-color: rgb(44, 86, 151); }
        """)
        self.ctgr3.setObjectName("ctgr3")
        self.ctgr3.clicked.connect(self.ctgr_three_clicked)
        self.ctgr4 = QtWidgets.QPushButton(ctg)
        self.ctgr4.setGeometry(QtCore.QRect(140, 440, 211, 41))
        self.ctgr4.setStyleSheet("""

            QPushButton:!hover { font-weight:490; background-color: white }
            QPushButton:hover { font-weight:490; color: rgb(255, 255, 255) ;background-color: rgb(44, 86, 151) }
            QPushButton:pressed { font-weight:490; color: rgb(255, 255, 255); background-color: rgb(44, 86, 151); }
        """)
        self.ctgr4.setObjectName("ctgr4")
        self.ctgr4.clicked.connect(self.ctgr_four_clicked)
        self.logo = QtWidgets.QLabel(ctg)
        self.logo.setGeometry(QtCore.QRect(10, 10, 461, 171))
        self.logo.setObjectName("logo")
        self.ctgr5 = QtWidgets.QPushButton(ctg)
        self.ctgr5.setGeometry(QtCore.QRect(140, 500, 211, 41))
        self.ctgr5.setStyleSheet("""

            QPushButton:!hover { font-weight:490; background-color: white }
            QPushButton:hover { font-weight:490; color: rgb(255, 255, 255) ;background-color: rgb(44, 86, 151) }
            QPushButton:pressed { font-weight:490; color: rgb(255, 255, 255); background-color: rgb(44, 86, 151); }
        """)
        self.ctgr5.clicked.connect(self.ctgr_five_clicked)
        self.ctgr5.setObjectName("ctgr5")
        self.ctgr6 = QtWidgets.QPushButton(ctg)
        self.ctgr6.setGeometry(QtCore.QRect(140, 560, 211, 41))
        self.ctgr6.setStyleSheet("""

            QPushButton:!hover { font-weight:490; background-color: white }
            QPushButton:hover { font-weight:490; color: rgb(255, 255, 255) ;background-color: rgb(44, 86, 151) }
            QPushButton:pressed { font-weight:490; color: rgb(255, 255, 255); background-color: rgb(44, 86, 151); }
        """)
        self.ctgr6.clicked.connect(self.ctgr_six_clicked)
        self.ctgr6.setObjectName("ctgr6")

        QtCore.QMetaObject.connectSlotsByName(ctg)

        self.retranslateUi(ctg)
        QtCore.QMetaObject.connectSlotsByName(ctg)

    def ctgr_one_clicked(self):
        Time_ctgr_one = QtWidgets.QDialog()
        ui1 = Ui_Time_ctgr_one()
        ui1.setupUi(Time_ctgr_one)
        Time_ctgr_one.show()
        Time_ctgr_one.exec()
    def ctgr_two_clicked(self):
        Time_ctgr_two = QtWidgets.QDialog()
        ui2 = Ui_Time_ctgr_two()
        ui2.setupUi(Time_ctgr_two)
        Time_ctgr_two.show()
        Time_ctgr_two.exec()

    def ctgr_three_clicked(self):
        Time_ctgr_three = QtWidgets.QDialog()
        ui3 = Ui_Time_ctgr_three()
        ui3.setupUi(Time_ctgr_three)
        Time_ctgr_three.show()
        Time_ctgr_three.exec()
    def ctgr_four_clicked(self):
        Time_ctgr_four = QtWidgets.QDialog()
        ui4 = Ui_Time_ctgr_four()
        ui4.setupUi(Time_ctgr_four)
        Time_ctgr_four.show()
        Time_ctgr_four.exec()
    def ctgr_five_clicked(self):
        Time_ctgr_five = QtWidgets.QDialog()
        ui5 = Ui_Time_ctgr_five()
        ui5.setupUi(Time_ctgr_five)
        Time_ctgr_five.show()
        Time_ctgr_five.exec()
    def ctgr_six_clicked(self):
        Time_ctgr_six = QtWidgets.QDialog()
        ui6 = Ui_Time_ctgr_six()
        ui6.setupUi(Time_ctgr_six)
        Time_ctgr_six.show()
        Time_ctgr_six.exec()
    def retranslateUi(self, ctg):
        _translate = QtCore.QCoreApplication.translate
        ctg.setWindowTitle(_translate("ctg", "NLMK Control"))
        self.logo.setText(_translate("ctg", "<html><head/><body><p align=\"center\"><img src=\":/newPrefix/nlmk_belyy_png (1).png\"/></p></body></html>"))
        self.text_select.setText(_translate("ctg", "<html><head/><body><p align=\"center\">Выберите категорию своей работы</p><p align=\"center\"><br/></p></body></html>"))
        self.ctgr1.setText(_translate("ctg", "Работа 1-ой категории"))
        self.ctgr2.setText(_translate("ctg", "Работа 2-ой категории"))
        self.ctgr3.setText(_translate("ctg", "Работа 3-ой категории"))
        self.ctgr4.setText(_translate("ctg", "Работа 4-ой категории"))
        self.ctgr5.setText(_translate("ctg", "Работа 5-ой категории"))
        self.ctgr6.setText(_translate("ctg", "Работа 6-ой категории"))


import cash_main_form_rc


class Ui_Time_ctgr_one(object):

    def setupUi(self, Time_ctgr_one):
        Time_ctgr_one.setObjectName("Time_ctgr_one")
        Time_ctgr_one.resize(480, 640)
        Time_ctgr_one.setStyleSheet("background-color: rgb(44, 86, 151);")


        self.lcdNumber = QtWidgets.QLCDNumber(Time_ctgr_one)
        self.lcdNumber.setGeometry(QtCore.QRect(10, 240, 451, 111))
        self.lcdNumber.setStyleSheet("color: rgb(255, 255, 255);")
        self.lcdNumber.setObjectName("lcdNumber")
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.updateLCD)
        self.timer.start(1000)
        self.text_1 = QtWidgets.QLabel(Time_ctgr_one)
        self.text_1.setGeometry(QtCore.QRect(10, 200, 431, 31))
        self.text_1.setStyleSheet("color: rgb(255, 255, 255);")
        self.text_1.setObjectName("text_1")
        self.text_2 = QtWidgets.QLabel(Time_ctgr_one)
        self.text_2.setGeometry(QtCore.QRect(10, 370, 451, 81))
        self.text_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.text_2.setObjectName("text_2")
        self.text_3 = QtWidgets.QLabel(Time_ctgr_one)
        self.text_3.setGeometry(QtCore.QRect(10, 10, 461, 181))
        self.text_3.setObjectName("text_3")
        self.text_4 = QtWidgets.QLabel(Time_ctgr_one)
        self.text_4.setGeometry(QtCore.QRect(10, 415, 451, 81))
        self.text_4.setStyleSheet("font:10pt; font-weight:600; color: rgb(255, 255, 255);")
        self.text_4.setObjectName("text_4")
        self.start = QtWidgets.QPushButton(Time_ctgr_one)
        self.start.setGeometry(QtCore.QRect(10, 520, 461, 41))
        self.start.setStyleSheet("""

            QPushButton:!hover { font-weight:490; background-color: white }
            QPushButton:hover { font-weight:490; color: rgb(255, 255, 255) ;background-color: rgb(44, 86, 151) }
            QPushButton:pressed { font-weight:490; color: rgb(255, 255, 255); background-color: rgb(44, 86, 151); }
        """)
        self.start.setObjectName("start")
        self.start.clicked.connect(self.button_start)
        self.finish = QtWidgets.QPushButton(Time_ctgr_one)
        self.finish.setGeometry(QtCore.QRect(10, 580, 461, 41))
        self.finish.setStyleSheet("""

            QPushButton:!hover { font-weight:490; background-color: white }
            QPushButton:hover { font-weight:490; color: rgb(255, 255, 255) ;background-color: rgb(44, 86, 151) }
            QPushButton:pressed { font-weight:490; color: rgb(255, 255, 255); background-color: rgb(44, 86, 151); }
        """)
        self.finish.setObjectName("finish")
        self.finish.clicked.connect(self.button_finish)
        self.retranslateUi(Time_ctgr_one)

        QtCore.QMetaObject.connectSlotsByName(Time_ctgr_one)


    def updateLCD(self):
        self.currentTime = QtCore.QTime.currentTime()
        self.strCurrentTime = self.currentTime.toString('HH:mm:ss')
        self.lcdNumber.display(self.strCurrentTime)
        self.lcdNumber.setDigitCount(8)
    def button_start(self):
        global start_time
        start_time = datetime.datetime.now()
        print('[1 Категория работ] Начало:',start_time, 'Ответственный:', id,  file=open("report.txt", "a"))
        self.text_4.setText('Работа начата. Желаем успехов!')
        return start_time
    def button_finish(self):
        finish_time = datetime.datetime.now()
        print('1',';',(finish_time - start_time).seconds,';',id, file=open("report.csv", "a"))
        print('[1 Категория работ] Завершение:',finish_time, 'Ответственный:', id, file=open("report.txt", "a"))
        print('[1 Категория работ] Длительность выполнения:', (finish_time - start_time).seconds,'секунд','Ответственный:', id, file=open("report.txt", "a"))
        app.exec()
        sys.exit(app.exec())
        #send_report('nlmk.org',"Employee","password")
        return finish_time




    def retranslateUi(self, Time_ctgr_one):

        _translate = QtCore.QCoreApplication.translate
        Time_ctgr_one.setWindowTitle(_translate("Time_ctgr_one", "NLMK Control"))
        self.text_1.setText(_translate("Time_ctgr_one", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Точное время:</span></p></body></html>"))
        self.text_2.setText(_translate("Time_ctgr_one", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Вы выбрали 1-ую категорию работ</span></p><p><span style=\" font-size:10pt; font-weight:600;\">Рекомендованное время выполнения: 5 минут (300 секунд)</span></p><p><span style=\" font-size:10pt; font-weight:600;\"><br/></span></p></body></html>"))
        self.text_3.setText(_translate("Time_ctgr_one", "<html><head/><body><p align=\"center\"><img src=\":/newPrefix/nlmk_belyy_png (1).png\"/></p></body></html>"))
        self.start.setText(_translate("Time_ctgr_one", "Начать работу"))
        self.finish.setText(_translate("Time_ctgr_one", "Завершить работу"))

class Ui_Time_ctgr_two(object):

    def setupUi(self, Time_ctgr_two):
        Time_ctgr_two.setObjectName("Time_ctgr_two")
        Time_ctgr_two.resize(480, 640)
        Time_ctgr_two.setStyleSheet("background-color: rgb(44, 86, 151);")


        self.lcdNumber = QtWidgets.QLCDNumber(Time_ctgr_two)
        self.lcdNumber.setGeometry(QtCore.QRect(10, 240, 451, 111))
        self.lcdNumber.setStyleSheet("color: rgb(255, 255, 255);")
        self.lcdNumber.setObjectName("lcdNumber")
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.updateLCD)
        self.timer.start(1000)
        self.text_1 = QtWidgets.QLabel(Time_ctgr_two)
        self.text_1.setGeometry(QtCore.QRect(10, 200, 431, 31))
        self.text_1.setStyleSheet("color: rgb(255, 255, 255);")
        self.text_1.setObjectName("text_1")
        self.text_2 = QtWidgets.QLabel(Time_ctgr_two)
        self.text_2.setGeometry(QtCore.QRect(10, 370, 451, 81))
        self.text_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.text_2.setObjectName("text_2")
        self.text_3 = QtWidgets.QLabel(Time_ctgr_two)
        self.text_3.setGeometry(QtCore.QRect(10, 10, 461, 181))
        self.text_3.setObjectName("text_3")
        self.text_4 = QtWidgets.QLabel(Time_ctgr_two)
        self.text_4.setGeometry(QtCore.QRect(10, 415, 451, 81))
        self.text_4.setStyleSheet("font:10pt; font-weight:600; color: rgb(255, 255, 255);")
        self.text_4.setObjectName("text_4")
        self.start = QtWidgets.QPushButton(Time_ctgr_two)
        self.start.setGeometry(QtCore.QRect(10, 520, 461, 41))
        self.start.setStyleSheet("""

            QPushButton:!hover { font-weight:490; background-color: white }
            QPushButton:hover { font-weight:490; color: rgb(255, 255, 255) ;background-color: rgb(44, 86, 151) }
            QPushButton:pressed { font-weight:490; color: rgb(255, 255, 255); background-color: rgb(44, 86, 151); }
        """)
        self.start.setObjectName("start")
        self.start.clicked.connect(self.button_start)
        self.finish = QtWidgets.QPushButton(Time_ctgr_two)
        self.finish.setGeometry(QtCore.QRect(10, 580, 461, 41))
        self.finish.setStyleSheet("""

            QPushButton:!hover { font-weight:490; background-color: white }
            QPushButton:hover { font-weight:490; color: rgb(255, 255, 255) ;background-color: rgb(44, 86, 151) }
            QPushButton:pressed { font-weight:490; color: rgb(255, 255, 255); background-color: rgb(44, 86, 151); }
        """)
        self.finish.setObjectName("finish")
        self.finish.clicked.connect(self.button_finish)
        self.retranslateUi(Time_ctgr_two)

        QtCore.QMetaObject.connectSlotsByName(Time_ctgr_two)

    def updateLCD(self):
        self.currentTime = QtCore.QTime.currentTime()
        self.strCurrentTime = self.currentTime.toString('HH:mm:ss')
        self.lcdNumber.display(self.strCurrentTime)
        self.lcdNumber.setDigitCount(8)
    def button_start(self):
        global start_time
        start_time = datetime.datetime.now()
        print('[2 Категория работ] Начало:',start_time, 'Ответственный:', id,  file=open("report.txt", "a"))
        self.text_4.setText('Работа начата. Желаем успехов!')
        return start_time
    def button_finish(self):
        finish_time = datetime.datetime.now()
        print('2',';',(finish_time - start_time).seconds,';',id, file=open("report.csv", "a"))
        print('[2 Категория работ] Завершение:',finish_time, 'Ответственный:', id, file=open("report.txt", "a"))
        print('[2 Категория работ] Длительность выполнения:', (finish_time - start_time).seconds,'секунд','Ответственный:', id, file=open("report.txt", "a"))
        app.exec()
        sys.exit(app.exec())
        #send_report('nlmk.org',"Employee","password")
        return finish_time




    def retranslateUi(self, Time_ctgr_two):

        _translate = QtCore.QCoreApplication.translate
        Time_ctgr_two.setWindowTitle(_translate("Time_ctgr_two", "NLMK Control"))
        self.text_1.setText(_translate("Time_ctgr_two", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Точное время:</span></p></body></html>"))
        self.text_2.setText(_translate("Time_ctgr_two", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Вы выбрали 2-ю категорию работ</span></p><p><span style=\" font-size:10pt; font-weight:600;\">Рекомендованное время выполнения: 10 минут (600 секунд)</span></p><p><span style=\" font-size:10pt; font-weight:600;\"><br/></span></p></body></html>"))
        self.text_3.setText(_translate("Time_ctgr_two", "<html><head/><body><p align=\"center\"><img src=\":/newPrefix/nlmk_belyy_png (1).png\"/></p></body></html>"))
        self.start.setText(_translate("Time_ctgr_two", "Начать работу"))
        self.finish.setText(_translate("Time_ctgr_two", "Завершить работу"))

class Ui_Time_ctgr_three(object):

    def setupUi(self, Time_ctgr_three):
        Time_ctgr_three.setObjectName("Time_ctgr_three")
        Time_ctgr_three.resize(480, 640)
        Time_ctgr_three.setStyleSheet("background-color: rgb(44, 86, 151);")


        self.lcdNumber = QtWidgets.QLCDNumber(Time_ctgr_three)
        self.lcdNumber.setGeometry(QtCore.QRect(10, 240, 451, 111))
        self.lcdNumber.setStyleSheet("color: rgb(255, 255, 255);")
        self.lcdNumber.setObjectName("lcdNumber")
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.updateLCD)
        self.timer.start(1000)
        self.text_1 = QtWidgets.QLabel(Time_ctgr_three)
        self.text_1.setGeometry(QtCore.QRect(10, 200, 431, 31))
        self.text_1.setStyleSheet("color: rgb(255, 255, 255);")
        self.text_1.setObjectName("text_1")
        self.text_2 = QtWidgets.QLabel(Time_ctgr_three)
        self.text_2.setGeometry(QtCore.QRect(10, 370, 451, 81))
        self.text_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.text_2.setObjectName("text_2")
        self.text_3 = QtWidgets.QLabel(Time_ctgr_three)
        self.text_3.setGeometry(QtCore.QRect(10, 10, 461, 181))
        self.text_3.setObjectName("text_3")
        self.text_4 = QtWidgets.QLabel(Time_ctgr_three)
        self.text_4.setGeometry(QtCore.QRect(10, 415, 451, 81))
        self.text_4.setStyleSheet("font:10pt; font-weight:600; color: rgb(255, 255, 255);")
        self.text_4.setObjectName("text_4")
        self.start = QtWidgets.QPushButton(Time_ctgr_three)
        self.start.setGeometry(QtCore.QRect(10, 520, 461, 41))
        self.start.setStyleSheet("""

            QPushButton:!hover { font-weight:490; background-color: white }
            QPushButton:hover { font-weight:490; color: rgb(255, 255, 255) ;background-color: rgb(44, 86, 151) }
            QPushButton:pressed { font-weight:490; color: rgb(255, 255, 255); background-color: rgb(44, 86, 151); }
        """)
        self.start.setObjectName("start")
        self.start.clicked.connect(self.button_start)
        self.finish = QtWidgets.QPushButton(Time_ctgr_three)
        self.finish.setGeometry(QtCore.QRect(10, 580, 461, 41))
        self.finish.setStyleSheet("""

            QPushButton:!hover { font-weight:490; background-color: white }
            QPushButton:hover { font-weight:490; color: rgb(255, 255, 255) ;background-color: rgb(44, 86, 151) }
            QPushButton:pressed { font-weight:490; color: rgb(255, 255, 255); background-color: rgb(44, 86, 151); }
        """)
        self.finish.setObjectName("finish")
        self.finish.clicked.connect(self.button_finish)
        self.retranslateUi(Time_ctgr_three)

        QtCore.QMetaObject.connectSlotsByName(Time_ctgr_three)

    def updateLCD(self):
        self.currentTime = QtCore.QTime.currentTime()
        self.strCurrentTime = self.currentTime.toString('HH:mm:ss')
        self.lcdNumber.display(self.strCurrentTime)
        self.lcdNumber.setDigitCount(8)
    def button_start(self):
        global start_time
        start_time = datetime.datetime.now()
        print('[3 Категория работ] Начало:',start_time, 'Ответственный:', id,  file=open("report.txt", "a"))
        self.text_4.setText('Работа начата. Желаем успехов!')
        return start_time
    def button_finish(self):
        finish_time = datetime.datetime.now()
        print('3',';',(finish_time - start_time).seconds,';',id, file=open("report.csv", "a"))
        print('[3 Категория работ] Завершение:',finish_time, 'Ответственный:', id, file=open("report.txt", "a"))
        print('[3 Категория работ] Длительность выполнения:', (finish_time - start_time).seconds,'секунд','Ответственный:', id, file=open("report.txt", "a"))
        app.exec()
        sys.exit(app.exec())
        #send_report('nlmk.org',"Employee","password")
        return finish_time




    def retranslateUi(self, Time_ctgr_three):

        _translate = QtCore.QCoreApplication.translate
        Time_ctgr_three.setWindowTitle(_translate("Time_ctgr_three", "NLMK Control"))
        self.text_1.setText(_translate("Time_ctgr_three", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Точное время:</span></p></body></html>"))
        self.text_2.setText(_translate("Time_ctgr_three", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Вы выбрали 3-ую категорию работ</span></p><p><span style=\" font-size:10pt; font-weight:600;\">Рекомендованное время выполнения: 15 минут (900 секунд)</span></p><p><span style=\" font-size:10pt; font-weight:600;\"><br/></span></p></body></html>"))
        self.text_3.setText(_translate("Time_ctgr_three", "<html><head/><body><p align=\"center\"><img src=\":/newPrefix/nlmk_belyy_png (1).png\"/></p></body></html>"))
        self.start.setText(_translate("Time_ctgr_three", "Начать работу"))
        self.finish.setText(_translate("Time_ctgr_three", "Завершить работу"))

class Ui_Time_ctgr_four(object):

    def setupUi(self, Time_ctgr_four):
        Time_ctgr_four.setObjectName("Time_ctgr_four")
        Time_ctgr_four.resize(480, 640)
        Time_ctgr_four.setStyleSheet("background-color: rgb(44, 86, 151);")


        self.lcdNumber = QtWidgets.QLCDNumber(Time_ctgr_four)
        self.lcdNumber.setGeometry(QtCore.QRect(10, 240, 451, 111))
        self.lcdNumber.setStyleSheet("color: rgb(255, 255, 255);")
        self.lcdNumber.setObjectName("lcdNumber")
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.updateLCD)
        self.timer.start(1000)
        self.text_1 = QtWidgets.QLabel(Time_ctgr_four)
        self.text_1.setGeometry(QtCore.QRect(10, 200, 431, 31))
        self.text_1.setStyleSheet("color: rgb(255, 255, 255);")
        self.text_1.setObjectName("text_1")
        self.text_2 = QtWidgets.QLabel(Time_ctgr_four)
        self.text_2.setGeometry(QtCore.QRect(10, 370, 451, 81))
        self.text_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.text_2.setObjectName("text_2")
        self.text_3 = QtWidgets.QLabel(Time_ctgr_four)
        self.text_3.setGeometry(QtCore.QRect(10, 10, 461, 181))
        self.text_3.setObjectName("text_3")
        self.text_4 = QtWidgets.QLabel(Time_ctgr_four)
        self.text_4.setGeometry(QtCore.QRect(10, 415, 451, 81))
        self.text_4.setStyleSheet("font:10pt; font-weight:600; color: rgb(255, 255, 255);")
        self.text_4.setObjectName("text_4")
        self.start = QtWidgets.QPushButton(Time_ctgr_four)
        self.start.setGeometry(QtCore.QRect(10, 520, 461, 41))
        self.start.setStyleSheet("""

            QPushButton:!hover { font-weight:490; background-color: white }
            QPushButton:hover { font-weight:490; color: rgb(255, 255, 255) ;background-color: rgb(44, 86, 151) }
            QPushButton:pressed { font-weight:490; color: rgb(255, 255, 255); background-color: rgb(44, 86, 151); }
        """)
        self.start.setObjectName("start")
        self.start.clicked.connect(self.button_start)
        self.finish = QtWidgets.QPushButton(Time_ctgr_four)
        self.finish.setGeometry(QtCore.QRect(10, 580, 461, 41))
        self.finish.setStyleSheet("""

            QPushButton:!hover { font-weight:490; background-color: white }
            QPushButton:hover { font-weight:490; color: rgb(255, 255, 255) ;background-color: rgb(44, 86, 151) }
            QPushButton:pressed { font-weight:490; color: rgb(255, 255, 255); background-color: rgb(44, 86, 151); }
        """)
        self.finish.setObjectName("finish")
        self.finish.clicked.connect(self.button_finish)
        self.retranslateUi(Time_ctgr_four)

        QtCore.QMetaObject.connectSlotsByName(Time_ctgr_four)

    def updateLCD(self):
        self.currentTime = QtCore.QTime.currentTime()
        self.strCurrentTime = self.currentTime.toString('HH:mm:ss')
        self.lcdNumber.display(self.strCurrentTime)
        self.lcdNumber.setDigitCount(8)

    def button_start(self):
        global start_time
        start_time = datetime.datetime.now()
        print('[4 Категория работ] Начало:', start_time, 'Ответственный:', id, file=open("report.txt", "a"))
        self.text_4.setText('Работа начата. Желаем успехов!')
        return start_time

    def button_finish(self):
        finish_time = datetime.datetime.now()
        print('4', ';', (finish_time - start_time).seconds, ';', id, file=open("report.csv", "a"))
        print('[4 Категория работ] Завершение:', finish_time, 'Ответственный:', id, file=open("report.txt", "a"))
        print('[4 Категория работ] Длительность выполнения:', (finish_time - start_time).seconds, 'секунд',
              'Ответственный:', id, file=open("report.txt", "a"))
        app.exec()
        sys.exit(app.exec())
        # send_report('nlmk.org',"Employee","password")
        return finish_time




    def retranslateUi(self, Time_ctgr_four):

        _translate = QtCore.QCoreApplication.translate
        Time_ctgr_four.setWindowTitle(_translate("Time_ctgr_four", "NLMK Control"))
        self.text_1.setText(_translate("Time_ctgr_four", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Точное время:</span></p></body></html>"))
        self.text_2.setText(_translate("Time_ctgr_four", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Вы выбрали 4-ую категорию работ</span></p><p><span style=\" font-size:10pt; font-weight:600;\">Рекомендованное время выполнения: 20 минут (1200 секунд)</span></p><p><span style=\" font-size:10pt; font-weight:600;\"><br/></span></p></body></html>"))
        self.text_3.setText(_translate("Time_ctgr_four", "<html><head/><body><p align=\"center\"><img src=\":/newPrefix/nlmk_belyy_png (1).png\"/></p></body></html>"))
        self.start.setText(_translate("Time_ctgr_four", "Начать работу"))
        self.finish.setText(_translate("Time_ctgr_four", "Завершить работу"))

class Ui_Time_ctgr_five(object):

    def setupUi(self, Time_ctgr_five):
        Time_ctgr_five.setObjectName("Time_ctgr_five")
        Time_ctgr_five.resize(480, 640)
        Time_ctgr_five.setStyleSheet("background-color: rgb(44, 86, 151);")


        self.lcdNumber = QtWidgets.QLCDNumber(Time_ctgr_five)
        self.lcdNumber.setGeometry(QtCore.QRect(10, 240, 451, 111))
        self.lcdNumber.setStyleSheet("color: rgb(255, 255, 255);")
        self.lcdNumber.setObjectName("lcdNumber")
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.updateLCD)
        self.timer.start(1000)
        self.text_1 = QtWidgets.QLabel(Time_ctgr_five)
        self.text_1.setGeometry(QtCore.QRect(10, 200, 431, 31))
        self.text_1.setStyleSheet("color: rgb(255, 255, 255);")
        self.text_1.setObjectName("text_1")
        self.text_2 = QtWidgets.QLabel(Time_ctgr_five)
        self.text_2.setGeometry(QtCore.QRect(10, 370, 451, 81))
        self.text_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.text_2.setObjectName("text_2")
        self.text_3 = QtWidgets.QLabel(Time_ctgr_five)
        self.text_3.setGeometry(QtCore.QRect(10, 10, 461, 181))
        self.text_3.setObjectName("text_3")
        self.text_4 = QtWidgets.QLabel(Time_ctgr_five)
        self.text_4.setGeometry(QtCore.QRect(10, 415, 451, 81))
        self.text_4.setStyleSheet("font:10pt; font-weight:600; color: rgb(255, 255, 255);")
        self.text_4.setObjectName("text_4")
        self.start = QtWidgets.QPushButton(Time_ctgr_five)
        self.start.setGeometry(QtCore.QRect(10, 520, 461, 41))
        self.start.setStyleSheet("""

            QPushButton:!hover { font-weight:490; background-color: white }
            QPushButton:hover { font-weight:490; color: rgb(255, 255, 255) ;background-color: rgb(44, 86, 151) }
            QPushButton:pressed { font-weight:490; color: rgb(255, 255, 255); background-color: rgb(44, 86, 151); }
        """)
        self.start.setObjectName("start")
        self.start.clicked.connect(self.button_start)
        self.finish = QtWidgets.QPushButton(Time_ctgr_five)
        self.finish.setGeometry(QtCore.QRect(10, 580, 461, 41))
        self.finish.setStyleSheet("""

            QPushButton:!hover { font-weight:490; background-color: white }
            QPushButton:hover { font-weight:490; color: rgb(255, 255, 255) ;background-color: rgb(44, 86, 151) }
            QPushButton:pressed { font-weight:490; color: rgb(255, 255, 255); background-color: rgb(44, 86, 151); }
        """)
        self.finish.setObjectName("finish")
        self.finish.clicked.connect(self.button_finish)
        self.retranslateUi(Time_ctgr_five)

        QtCore.QMetaObject.connectSlotsByName(Time_ctgr_five)

    def updateLCD(self):
        self.currentTime = QtCore.QTime.currentTime()
        self.strCurrentTime = self.currentTime.toString('HH:mm:ss')
        self.lcdNumber.display(self.strCurrentTime)
        self.lcdNumber.setDigitCount(8)
    def button_start(self):
        global start_time
        start_time = datetime.datetime.now()
        print('[5 Категория работ] Начало:',start_time, 'Ответственный:', id,  file=open("report.txt", "a"))
        self.text_4.setText('Работа начата. Желаем успехов!')
        return start_time
    def button_finish(self):
        finish_time = datetime.datetime.now()
        print('5',';',(finish_time - start_time).seconds,';',id, file=open("report.csv", "a"))
        print('[5 Категория работ] Завершение:',finish_time, 'Ответственный:', id, file=open("report.txt", "a"))
        print('[5 Категория работ] Длительность выполнения:', (finish_time - start_time).seconds,'секунд','Ответственный:', id, file=open("report.txt", "a"))
        app.exec()
        sys.exit(app.exec())
        #send_report('nlmk.org',"Employee","password")
        return finish_time



    def retranslateUi(self, Time_ctgr_five):

        _translate = QtCore.QCoreApplication.translate
        Time_ctgr_five.setWindowTitle(_translate("Time_ctgr_five", "NLMK Control"))
        self.text_1.setText(_translate("Time_ctgr_five", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Точное время:</span></p></body></html>"))
        self.text_2.setText(_translate("Time_ctgr_five", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Вы выбрали 5-ую категорию работ</span></p><p><span style=\" font-size:10pt; font-weight:600;\">Рекомендованное время выполнения: 25 минут (1500 секунд)</span></p><p><span style=\" font-size:10pt; font-weight:600;\"><br/></span></p></body></html>"))
        self.text_3.setText(_translate("Time_ctgr_five", "<html><head/><body><p align=\"center\"><img src=\":/newPrefix/nlmk_belyy_png (1).png\"/></p></body></html>"))
        self.start.setText(_translate("Time_ctgr_five", "Начать работу"))
        self.finish.setText(_translate("Time_ctgr_five", "Завершить работу"))

class Ui_Time_ctgr_six(object):

    def setupUi(self, Time_ctgr_six):
        Time_ctgr_six.setObjectName("Time_ctgr_six")
        Time_ctgr_six.resize(480, 640)
        Time_ctgr_six.setStyleSheet("background-color: rgb(44, 86, 151);")


        self.lcdNumber = QtWidgets.QLCDNumber(Time_ctgr_six)
        self.lcdNumber.setGeometry(QtCore.QRect(10, 240, 451, 111))
        self.lcdNumber.setStyleSheet("color: rgb(255, 255, 255);")
        self.lcdNumber.setObjectName("lcdNumber")
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.updateLCD)
        self.timer.start(1000)
        self.text_1 = QtWidgets.QLabel(Time_ctgr_six)
        self.text_1.setGeometry(QtCore.QRect(10, 200, 431, 31))
        self.text_1.setStyleSheet("color: rgb(255, 255, 255);")
        self.text_1.setObjectName("text_1")
        self.text_2 = QtWidgets.QLabel(Time_ctgr_six)
        self.text_2.setGeometry(QtCore.QRect(10, 370, 451, 81))
        self.text_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.text_2.setObjectName("text_2")
        self.text_3 = QtWidgets.QLabel(Time_ctgr_six)
        self.text_3.setGeometry(QtCore.QRect(10, 10, 461, 181))
        self.text_3.setObjectName("text_3")
        self.text_4 = QtWidgets.QLabel(Time_ctgr_six)
        self.text_4.setGeometry(QtCore.QRect(10, 415, 451, 81))
        self.text_4.setStyleSheet("font:10pt; font-weight:600; color: rgb(255, 255, 255);")
        self.text_4.setObjectName("text_4")
        self.start = QtWidgets.QPushButton(Time_ctgr_six)
        self.start.setGeometry(QtCore.QRect(10, 520, 461, 41))
        self.start.setStyleSheet("""

            QPushButton:!hover { font-weight:490; background-color: white }
            QPushButton:hover { font-weight:490; color: rgb(255, 255, 255) ;background-color: rgb(44, 86, 151) }
            QPushButton:pressed { font-weight:490; color: rgb(255, 255, 255); background-color: rgb(44, 86, 151); }
        """)
        self.start.setObjectName("start")
        self.start.clicked.connect(self.button_start)
        self.finish = QtWidgets.QPushButton(Time_ctgr_six)
        self.finish.setGeometry(QtCore.QRect(10, 580, 461, 41))
        self.finish.setStyleSheet("""

            QPushButton:!hover { font-weight:490; background-color: white }
            QPushButton:hover { font-weight:490; color: rgb(255, 255, 255) ;background-color: rgb(44, 86, 151) }
            QPushButton:pressed { font-weight:490; color: rgb(255, 255, 255); background-color: rgb(44, 86, 151); }
        """)
        self.finish.setObjectName("finish")
        self.finish.clicked.connect(self.button_finish)
        self.retranslateUi(Time_ctgr_six)

        QtCore.QMetaObject.connectSlotsByName(Time_ctgr_six)

    def updateLCD(self):
        self.currentTime = QtCore.QTime.currentTime()
        self.strCurrentTime = self.currentTime.toString('HH:mm:ss')
        self.lcdNumber.display(self.strCurrentTime)
        self.lcdNumber.setDigitCount(8)
    def button_start(self):
        global start_time
        start_time = datetime.datetime.now()
        print('[6 Категория работ] Начало:',start_time, 'Ответственный:', id,  file=open("report.txt", "a"))
        self.text_4.setText('Работа начата. Желаем успехов!')
        return start_time
    def button_finish(self):
        finish_time = datetime.datetime.now()
        print('6',';',(finish_time - start_time).seconds,';',id, file=open("report.csv", "a"))
        print('[6 Категория работ] Завершение:',finish_time, 'Ответственный:', id, file=open("report.txt", "a"))
        print('[6 Категория работ] Длительность выполнения:', (finish_time - start_time).seconds,'секунд','Ответственный:', id, file=open("report.txt", "a"))
        app.exec()
        sys.exit(app.exec())
        #send_report('nlmk.org',"Employee","password")
        return finish_time



    def retranslateUi(self, Time_ctgr_six):

        _translate = QtCore.QCoreApplication.translate
        Time_ctgr_six.setWindowTitle(_translate("Time_ctgr_six", "NLMK Control"))
        self.text_1.setText(_translate("Time_ctgr_six", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Точное время:</span></p></body></html>"))
        self.text_2.setText(_translate("Time_ctgr_six", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Вы выбрали 6-ую категорию работ</span></p><p><span style=\" font-size:10pt; font-weight:600;\">Рекомендованное время выполнения: 30 минут (1800 секунд)</span></p><p><span style=\" font-size:10pt; font-weight:600;\"><br/></span></p></body></html>"))
        self.text_3.setText(_translate("Time_ctgr_six", "<html><head/><body><p align=\"center\"><img src=\":/newPrefix/nlmk_belyy_png (1).png\"/></p></body></html>"))
        self.start.setText(_translate("Time_ctgr_six", "Начать работу"))
        self.finish.setText(_translate("Time_ctgr_six", "Завершить работу"))

import cash_time_form_rc

#def send_report(host,ftp_user,ftp_password):
#    filename = "report.txt"
#    con = ftplib.FTP(host, ftp_user, ftp_password)
#    f = open(filename, "rb")
#    send = con.storbinary("STOR " + filename, f)
#    con.close

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    global ui
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.exec()
    sys.exit(app.exec())

