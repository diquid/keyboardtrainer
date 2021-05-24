from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from menu import *
from recordtable import *
from typewindow import *

Form, Window = uic.loadUiType("menu.ui")

app = QApplication([])
window = QtWidgets.QMainWindow()
form = Form()
ui = Ui_MainWindow()
ui.setupUi(window)
#form.setupUi(window)
window.show()

def start(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow1()
        self.ui.setup(self.window)
        self.window.show()

def recordtable(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow2()
        self.ui.setup2(self.window)
        self.window.show()


ui.startbutton.clicked.connect(start)   
app.exec()