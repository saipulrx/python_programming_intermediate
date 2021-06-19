import sys
import os
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUi

class MainForm(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self,parent)
        # load file .ui yg dibuat di qt designer
        loadUi("/Users/muhammadsaipulrohman/Documents/IDB/source_code/qtDesigner/demoQDialogOpenDir.ui",self)

        self.pushButton.clicked.connect(self.OpenDirClick)

    def OpenDirClick(self):
        dirName = QFileDialog.getExistingDirectory(self,'Pilih Direktori',os.curdir,QFileDialog.ShowDirsOnly)
        if not dirName: return
        self.lineEdit.setText(dirName)
        model = QFileSystemModel()
        model.setRootPath(dirName)
        model.setFilter(QDir.AllDirs | QDir.Files)
        self.treeView.setModel(model)
        self.treeView.setRootIndex(model.index(dirName))

if __name__ == "__main__":
    a = QApplication(sys.argv)
    form = MainForm()
    form.show()
    a.exec_()   