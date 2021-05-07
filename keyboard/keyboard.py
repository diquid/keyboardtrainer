from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("Клавиатурный тренажер")
        self.setGeometry(300, 250, 1000, 700)

        self.new_text = QtWidgets.QLabel(self)

        self.main_text = QtWidgets.QLabel(self)
        self.main_text.setText("ibvpibvsibvs")
        self.main_text.move(100, 100)
        self.main_text.adjustSize()

        self.btn1 = QtWidgets.QPushButton(self)
        self.btn1.move(400, 150)
        self.btn1.setText("Старт")
        self.btn1.setFixedWidth(200)
        self.btn1.clicked.connect(self.add_label)

        self.btn2 = QtWidgets.QPushButton(self)
        self.btn2.move(400, 250)  
        self.btn2.setText("Таблица рекордов")
        self.btn2.setFixedWidth(200)
        #btn.clicked.connect(add_label)

    def add_label(self):
        self.new_text.setText("Вторая надпись")
        self.new_text.move(100, 50)
        self.new_text.adjustSize()

def application():
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()
