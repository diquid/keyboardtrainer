from PyQt5.QtWidgets import QTextEdit
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import Qt

from aftertype import Ui_Dialog3


class TextEditor(QTextEdit):
    def __init__(self, parent, text):
        super().__init__(parent)
        self.ref_text = ''
        self.index = 0

    def set_ref_text(self, text):
        self.ref_text = text

    def aftertype(self):
        self.Dialog = QtWidgets.QDialog()
        self.ui = Ui_Dialog3()
        self.ui.setup3(self.Dialog)
        self.Dialog.show()

    def keyPressEvent(self, e) -> None:
        # typed_text = self.textEdit.toPlainText()
        # index = len(typed_text) - 1
        key = e.text()
        max_index = len(self.ref_text)
        if (e.key() == Qt.Key_Shift) | (e.key() == Qt.Key_Alt):
            pass
        elif e.key() == Qt.Key_Backspace:
            self.index -= 1
        else:
            if key == self.ref_text[self.index]:
               self.setTextColor(QtGui.QColor("green"))
            else:
               self.setTextColor(QtGui.QColor("red"))
            self.index += 1

        if self.index == max_index:
            self.aftertype()
        QTextEdit.keyPressEvent(self, e)
