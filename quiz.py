from functools import update_wrapper
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import os
import sys
import random
from datetime import datetime
from db import *
from Worker import *
from time import time,sleep
from fuzzywuzzy import process
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(601, 530)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ru_phrase = QtWidgets.QLabel(self.centralwidget)
        self.ru_phrase.setGeometry(QtCore.QRect(20, 160, 561, 161))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ru_phrase.sizePolicy().hasHeightForWidth())
        self.ru_phrase.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Bitstream Vera Sans")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.ru_phrase.setFont(font)
        self.ru_phrase.setStyleSheet("background-color: rgb(153, 193, 241);\n"
        "border-radius: 25px;\n"
        "")
        self.ru_phrase.setText("")
        self.ru_phrase.setTextFormat(QtCore.Qt.MarkdownText)
        self.ru_phrase.setScaledContents(True)
        self.ru_phrase.setAlignment(QtCore.Qt.AlignCenter)
        self.ru_phrase.setWordWrap(True)
        self.ru_phrase.setObjectName("ru_phrase")
        self.en_phrase = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.en_phrase.setGeometry(QtCore.QRect(20, 330, 561, 141))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.en_phrase.setFont(font)
        self.en_phrase.setPlainText("")
        self.en_phrase.setObjectName("en_phrase")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(160, 0, 431, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(230, 20, 361, 31))
        self.label_2.setText("")
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.ru_word = QtWidgets.QLabel(self.centralwidget)
        self.ru_word.setGeometry(QtCore.QRect(21, 71, 271, 81))
        font = QtGui.QFont()
        font.setFamily("FreeSans")
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        self.ru_word.setFont(font)
        self.ru_word.setStyleSheet(" border-radius: 25px;\n"
        "background-color: rgb(53, 132, 228);")
        self.ru_word.setText("")
        self.ru_word.setTextFormat(QtCore.Qt.PlainText)
        self.ru_word.setAlignment(QtCore.Qt.AlignCenter)
        self.ru_word.setWordWrap(True)
        self.ru_word.setObjectName("ru_word")
        self.en_word = QtWidgets.QLabel(self.centralwidget)
        self.en_word.setGeometry(QtCore.QRect(310, 70, 271, 81))
        font = QtGui.QFont()
        font.setFamily("FreeMono")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.en_word.setFont(font)
        self.en_word.setAutoFillBackground(False)
        self.en_word.setStyleSheet("background-color: rgb(237, 51, 59);\n"
            " border-radius: 25px;\n"
            "")
        self.en_word.setText("")
        self.en_word.setTextFormat(QtCore.Qt.PlainText)
        self.en_word.setAlignment(QtCore.Qt.AlignCenter)
        self.en_word.setWordWrap(True)
        self.en_word.setObjectName("en_word")
        self.submit = QtWidgets.QPushButton(self.centralwidget)
        self.submit.setGeometry(QtCore.QRect(250, 480, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.submit.setFont(font)
        self.submit.setStyleSheet("color: rgb(246, 245, 244);\n"
            "background-color: rgb(98, 160, 234);\n"
            " border-radius: 10px;\n"
            "")
        self.submit.setObjectName("submit")
        self.clear = QtWidgets.QPushButton(self.centralwidget)
        self.clear.setGeometry(QtCore.QRect(131, 480, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.clear.setFont(font)
        self.clear.setStyleSheet("color: rgb(246, 245, 244);\n"
            "background-color: rgb(224, 27, 36);\n"
            " border-radius: 10px;\n"
            "")
        self.clear.setObjectName("clear")
        self.next = QtWidgets.QPushButton(self.centralwidget)
        self.next.setGeometry(QtCore.QRect(370, 480, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.next.setFont(font)
        self.next.setStyleSheet("color: rgb(246, 245, 244);\n"
            "background-color: rgb(51, 209, 122);\n"
            " border-radius: 10px;")
        self.next.setObjectName("next")
        self.skip = QtWidgets.QPushButton(self.centralwidget)
        self.skip.setGeometry(QtCore.QRect(270, 70, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.skip.setFont(font)
        self.skip.setStyleSheet("color: rgb(255, 255, 255);\n"
            "background-color: rgb(165, 29, 45);\n"
            "/*background-color: rgb(46, 194, 126);\n"
            "background-color: rgb(0, 0, 0);*/\n"
            " border-radius: 10px;\n"
            "")
        self.skip.setObjectName("skip")
        #self.add_to_important = QtWidgets.QPushButton(self.centralwidget)
        #self.add_to_important.setGeometry(QtCore.QRect(250, 70, 21, 21))
        #font = QtGui.QFont()
        #font.setPointSize(14)
        #font.setBold(True)
        #font.setWeight(75)
        #self.add_to_important.setFont(font)
        #self.add_to_important.setStyleSheet("color: rgb(255, 255, 255);\n"
        #    "background-color: rgb(46, 194, 126);\n"
        #    "/*background-color: rgb(0, 0, 0);*/\n"
        #    " border-radius: 10px;\n"
        #    "")
        #self.add_to_important.setObjectName("add_to_important")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Common Russian Vocabulary V1.0"))
        self.label.setText(_translate("MainWindow", "unknown  |   Level : 1    |   Points : 0"))
        self.submit.setText(_translate("MainWindow", "submit "))
        self.clear.setText(_translate("MainWindow", "clear"))
        self.next.setText(_translate("MainWindow", "Next >>"))
        self.skip.setText(_translate("MainWindow", "X"))
        #self.add_to_important.setText(_translate("MainWindow", "+"))
        self.init()

    def init(self):
        self.submit.clicked.connect(self.submit_clicked)
        self.clear.clicked.connect(self.clear_clicked)
        self.next.clicked.connect(self.next_clicked)
        self.skip.clicked.connect(self.skip_clicked)
        #self.add_to_important.clicked.connect(self.add_to_important_clicked)
        self.answer = self.init_controls()

    def init_controls(self):
        self.next.setDisabled(True)
        self.info()
        self.deslock_controls()
        self.en_phrase.setStyleSheet("background-color: rgb(255, 255, 255);\n")
        words = db.get_words()
        if words != None:
            index = random.randint(0,99)
            word = words[index]
            self.ru_word.setText(" | \n".join(word[1].split(';')))
            self.ru_phrase.setText(" | \n".join(word[3].split(';')))
            if word[4]!="" and int(word[5])<100:
                self.en_word.setText(" | \n".join(word[2].split(';')))
            else:
                self.en_word.setText("? ? ? ?")
            return word
        return None
        
    def submit_clicked(self):
        ratio = self.check_ratio_true(self.en_phrase.toPlainText().lower())
        self.lock_controls()
        self.next.setDisabled(False)
        if self.answer != None:
            id = int(self.answer[0])
            if self.answer[4]!="":
                if ratio>=80:
                    db.update_words({'id':id},{'point':int(self.answer[5])+(int(self.answer[5])//100)*10,'date':str(datetime.now())[:10]})
                    self.en_phrase.setStyleSheet("background-color: rgba(57, 172, 85, 133);\ncolor:rgb(255,255,255);\n")
                else:
                    db.update_words({'id':id},{'failure':int(self.answer[7])+1})
                    self.en_phrase.setStyleSheet("background-color: rgba(247, 66, 66, 151);\ncolor:rgb(255,255,255);\n")
                self.en_phrase.setPlainText("\n".join(self.answer[4].split(';')))
        self.info()
        
    def add_to_important_clicked(self):
        pass

    def next_clicked(self):
        self.info()
        self.clear_clicked()
        self.answer = self.init_controls()
        self.deslock_controls()
    
    def clear_clicked(self):
        self.en_phrase.clear()
    
    def skip_clicked(self):
        db.update_words({'id':self.answer[0]},{'point':'500','failure':0})
        self.answer = self.init_controls()
        
    def lock_controls(self):
        self.submit.setDisabled(True)
        self.en_phrase.setDisabled(True)
        self.next.setDisabled(False)

    def deslock_controls(self):
        self.submit.setDisabled(False)
        self.en_phrase.setDisabled(False)
        self.next.setDisabled(True)

    def info(self):
        lvl = db.get_level()
        info = f" {db.get_user()}  | Level: {lvl[0]}  | Points: {lvl[1]}  "
        self.label.setText(info)

    def check_ratio_true(self,answer):
        
        if self.answer[4]!="":
            options = self.answer[4]
        else:
            options = self.answer[2]
        ratio = process.extract(answer,options.split(';'))
        print(ratio)
        return sum([x[1] for x in ratio if len(ratio)>0])/len(ratio)
        #if answer in position_answer.split(';'):
        #        return 100
        #else:
        #    pass
        #    phrase_en = position_answer.replace(';',' ')
        #    phrase_en = list(set(phrase_en.split(' ')))
        #    ret = 0
        #    ans = set(answer.split(' '))
        #    for word in ans:
        #        if word in phrase_en:
        #            ret+=1
        #    return ret*100//len(ans)
        #return 0


