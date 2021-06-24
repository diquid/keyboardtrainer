from PyQt5.QtWidgets import QTextEdit
from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import Qt

from aftertype import Ui_Dialog3


class TextEditor(QTextEdit):
    def __init__(self, parent, text):
        super().__init__(parent)
        self.ref_text = ''
        self.index = 0
        self.errors_counter = 0
        self.is_incorrect = False

    def set_ref_text(self, text):
        self.ref_text = text

    def aftertype(self):
        self.Dialog = QtWidgets.QDialog()
        self.ui = Ui_Dialog3()
        self.ui.setup3(self.Dialog)
        self.Dialog.show()

    def keyPressEvent(self, e) -> None:
        key = e.text()
        max_index = len(self.ref_text)
        if (e.key() == Qt.Key_Shift) | (e.key() == Qt.Key_Alt):
            pass
        elif e.key() == Qt.Key_Backspace:
            self.index -= 1
            if self.is_incorrect:
                self.errors_counter -= 1
                self.is_incorrect = False
            else:
                pass
        else:
            if key == self.ref_text[self.index]:
                self.setTextColor(QtGui.QColor("green"))
                self.is_incorrect = False
            else:
                self.setTextColor(QtGui.QColor("red"))
                self.errors_counter += 1
                self.is_incorrect = True
            self.index += 1
        print(self.errors_counter)
        self.show_errors()
        if max_index - self.index == 1:
            self.aftertype()
        QTextEdit.keyPressEvent(self, e)

    def show_errors(self):
        errors = self.errors_counter
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(50, 630, 500, 31))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setText("Количество ошибок: " + str(errors))
        self.label_3.setObjectName("label_3")
