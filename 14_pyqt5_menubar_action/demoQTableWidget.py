import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUi

class FormQTableWidget(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self,parent)
        # load file .ui yg dibuat di qt designer
        loadUi("/Users/muhammadsaipulrohman/Documents/IDB/source_code/qtDesigner/demoQTableWidget.ui",self)

        self.tableWidget.itemClicked.connect(self.tableItemClick)

    def tableItemClick(self):
        item = self.tableWidget.currentItem()
        self.lineEdit.setText(item.text() + ' [ baris: %d, kolom: %d]' %
        (self.tableWidget.currentRow(), self.tableWidget.currentColumn()))

if __name__ == "__main__":
    a = QApplication(sys.argv)
    form = FormQTableWidget()
    form.show()
    a.exec_()     