# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import typewindow
from recordtable import *
from textread import *
from aftertype import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QHBoxLayout, QLabel
from PyQt5.QtGui import QIcon, QPixmap
from playsound import playsound
import multiprocessing
from threading import Thread


# paused = False    # global to track if the audio is paused
# def on_press(key):
#     global paused
#     print (key)
#     if key == keyboard.Key.space:
#         if stream.is_stopped():     # time to play audio
#             print ('play pressed')
#             stream.start_stream()
#             paused = False
#             return False
#         elif stream.is_active():   # time to pause audio
#             print ('pause pressed')
#             stream.stop_stream()
#             paused = True
#             return False
#     return False
#
#
# # you audio here
# wf = open('SLAVA_MARLOW_-_Snova_ya_napivayus.mp3', 'rb')
#
# # instantiate PyAudio
# p = pyaudio.PyAudio()
#
# # define callback
# def callback(in_data, frame_count, time_info, status):
#     data = wf.readframes(frame_count)
#     return (data, pyaudio.paContinue)
#
# # open stream using callback
# stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
#                 channels=wf.getnchannels(),
#                 rate=wf.getframerate(),
#                 output=True,
#                 stream_callback=callback)
#
# # start the stream
# stream.start_stream()
#
# while stream.is_active() or paused==True:
#     with keyboard.Listener(on_press=on_press) as listener:
#         listener.join()
#     time.sleep(0.1)
#
# # stop stream
# stream.stop_stream()
# stream.close()
# wf.close()
#
# # close PyAudio
# p.terminate()

#playsound('SLAVA_MARLOW_-_Snova_ya_napivayus.mp3')


class Ui_MainWindow(object):

    def start(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = typewindow.Ui_MainWindow1()
        self.ui.setup1(self.window)
        self.window.show()

    def records(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow4()
        self.ui.setup4(self.window)
        self.window.show()

    def menu(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def play(self):
        playsound('SLAVA_MARLOW_-_Snova_ya_napivayus.mp3')
        #winsound.PlaySound(r'SLAVA_MARLOW_-_Snova_ya_napivayus.mp3', winsound.SND_ASYNC)
        #thread1 = Thread(target=playsound, args=("SLAVA_MARLOW_-_Snova_ya_napivayus.mp3.mp3",))
        #thread1.start()
        #thread1.join()
        #input("press ENTER to stop playback")

    def pause(self):
        playsound('SLAVA_MARLOW_-_Snova_ya_napivayus.mp3')

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.startbutton = QtWidgets.QPushButton(self.centralwidget)
        self.startbutton.setGeometry(QtCore.QRect(340, 210, 301, 71))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(142, 142, 213))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(142, 142, 213))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(142, 142, 213))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        #hbox = QHBoxLayout(self)
        #pixmap = QPixmap("1pic.jpg")
        #lbl = QLabel(self)
        #lbl.setPixmap(pixmap)
        #hbox.addWidget(lbl)
        #self.setLayout(hbox)

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        pixmap = QPixmap('20pic.png')
        self.label_3.setPixmap(pixmap)
        self.label_3.setObjectName("label_3")
        self.label_3.move(150, 360)

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        pixmap = QPixmap('30pic.png')
        self.label_4.setPixmap(pixmap)
        self.label_4.setObjectName("label_3")
        self.label_4.move(670, 300)


        self.startbutton.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(14)
        self.startbutton.setFont(font)
        self.startbutton.setObjectName("startbutton")
        self.startbutton.clicked.connect(self.start)


        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 20, 461, 81))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(28)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")


        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(160, 70, 650, 71))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(28)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")


        self.recordsbutton = QtWidgets.QPushButton(self.centralwidget)
        self.recordsbutton.setGeometry(QtCore.QRect(340, 300, 301, 71))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(14)
        self.recordsbutton.setFont(font)
        self.recordsbutton.setObjectName("recordsbutton")
        self.recordsbutton.clicked.connect(self.records)

        self.exitbutton = QtWidgets.QPushButton(self.centralwidget)
        self.exitbutton.setGeometry(QtCore.QRect(340, 390, 301, 71))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(14)
        self.exitbutton.setFont(font)
        self.exitbutton.setObjectName("exitbutton")
        self.exitbutton.clicked.connect(quit)


        self.playbutton = QtWidgets.QPushButton(self.centralwidget)
        self.playbutton.setGeometry(QtCore.QRect(830, 600, 50, 50))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(14)
        self.playbutton.setFont(font)
        self.playbutton.setObjectName("playbutton")
        self.playbutton.clicked.connect(self.play)


        self.pausebutton = QtWidgets.QPushButton(self.centralwidget)
        self.pausebutton.setGeometry(QtCore.QRect(900, 600, 50, 50))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(14)
        self.pausebutton.setFont(font)
        self.pausebutton.setObjectName("pausebutton")
        self.pausebutton.clicked.connect(self.pause)


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)


        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.startbutton.setText(_translate("MainWindow", "Старт"))
        self.label.setText(_translate("MainWindow", "Добро пожаловать"))
        self.label_2.setText(_translate("MainWindow", "в клавиатурный тренажер!"))
        self.recordsbutton.setText(_translate("MainWindow", "Таблица рекордов"))
        self.exitbutton.setText(_translate("MainWindow", "Выход"))
        self.playbutton.setText(_translate("MainWindow", "►"))
        self.pausebutton.setText(_translate("MainWindow", "◼"))

    def quit(self):
        sys.exit()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    sys.exit(app.exec_())