import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUi

class MainForm(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self,parent)
        # load file .ui yg dibuat di qt designer
        loadUi("/Users/muhammadsaipulrohman/Documents/IDB/source_code/qtDesigner/demoQFontDialog.ui",self)

        self.pushButton.clicked.connect(self.FontButtonClick)

    def FontButtonClick(self):
        fontTuple = QFontDialog.getFont(QFont('Arial', 11), self, 'Pilih Font')
        if fontTuple[0]:
            self.textEdit.setCurrentFont(fontTuple[0])

if __name__ == "__main__":
    a = QApplication(sys.argv)
    form = MainForm()
    form.show()
    a.exec_()