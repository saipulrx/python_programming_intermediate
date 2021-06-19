import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUi

class MainForm(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self,parent)
        # load file .ui yg dibuat di qt designer
        loadUi("/Users/muhammadsaipulrohman/Documents/IDB/source_code/qtDesigner/demoQColorDialog.ui",self)

        self.pushButton.clicked.connect(self.colorButtonClick)

    def colorButtonClick(self):
        color = QColorDialog.getColor(Qt.black,self,'Pilih Warna')
        if color:
            self.textEdit.setTextColor(color)

if __name__ == "__main__":
    a = QApplication(sys.argv)
    form = MainForm()
    form.show()
    a.exec_()