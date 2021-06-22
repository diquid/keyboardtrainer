import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from typewindow import *
from menu import *
from recordtable import *



def timer_handler():
        time = time.addSecs(1)
        print(time.toString("mm:ss"))


if __name__ == "__main__":
    app = QtCore.QCoreApplication(sys.argv)
    timer = QtCore.QTimer()
    elapsed_time = QtCore.QTime(0, 0, 0)
    timer.setInterval(1000)
    timer.timeout.connect(timer_handler)
    timer.start()
    sys.exit(app.exec_())




