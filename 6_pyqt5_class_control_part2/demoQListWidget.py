import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUi

class MainForm(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self,parent)
        # load file .ui yg dibuat di qt designer
        loadUi("/Users/muhammadsaipulrohman/Documents/IDB/source_code/qtDesigner/demoQListWidget.ui",self)

        self.btnAdd.clicked.connect(self.btnAddClick)
        self.btnRight.clicked.connect(self.btnRightClick)
        self.btnRightAll.clicked.connect(self.btnRightAllClick)
        self.btnLeft.clicked.connect(self.btnLeftClick)
        self.btnLeftAll.clicked.connect(self.btnLeftAllClick)

    def btnAddClick(self):
        if len(self.txtElement.text()) == 0: return
        item = self.txtElement.text()
        self.list1.addItem(item)
        self.txtElement.clear()
        self.txtElement.setFocus()

    def btnRightClick(self):
        if self.list1.currentRow() < 0: return
        self.list2.addItem(self.list1.currentItem().text())
        self.list1.takeItem(self.list1.currentRow())

    def btnRightAllClick(self):
        for index in range(self.list1.count()):
            self.list2.addItem(self.list1.item(index).text())
        self.list1.clear()

    def btnLeftClick(self):
        if self.list2.currentRow() < 0: return
        self.list1.addItem(self.list2.currentItem().text())
        self.list2.takeItem(self.list1.currentRow())

    def btnLeftAllClick(self):
        for index in range(self.list2.count()):
            self.list1.addItem(self.list2.item(index).text())
        self.list2.clear()

if __name__ == "__main__":
    a = QApplication(sys.argv)
    form = MainForm()
    form.show()
    a.exec_() 