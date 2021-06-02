from PyQt5 import QtCore, QtGui, QtWidgets
import random
import time
import os
from shutil import get_terminal_size
import sys
from typewindow import *
from recordtable import *
from menu import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton
from PyQt5.QtGui import QIcon


class textread_1(object):

    def textread(self):
        s =""
        text = open('baza.txt', 'r').read()
        with open('baza.txt') as f:
            line_count = 0
            for line in f:
                line_count += 1
        random1 = random.randint(1, line_count)
        textf = open('baza.txt').readlines()
        length_textf = len(textf)
        line = textf[random1 - 1]

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow1()
    ui.setup1(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())




