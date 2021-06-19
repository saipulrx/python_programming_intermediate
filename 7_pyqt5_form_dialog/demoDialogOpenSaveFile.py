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
        loadUi("/Users/muhammadsaipulrohman/Documents/IDB/source_code/qtDesigner/dialogOpenFile.ui",self)

        self.pushButton.clicked.connect(self.openFileClick)
        self.btnSimpan.clicked.connect(self.saveFileClick)

    def openFileClick(self):
        filename = QFileDialog.getOpenFileName(self,'Pilih File',os.curdir,
        'Python Code (*.py);; PHP Code (*.php)','*.py')
        if not filename[0]: return
        self.label.setText('Nama File: ' + filename[0])
        fileHandle = QFile(filename[0])
        if not fileHandle.open(QIODevice.ReadOnly): return
        stream = QTextStream(fileHandle)
        self.textEdit.setPlainText(stream.readAll())
        fileHandle.close()

    def saveFileClick(self):
        filename = QFileDialog.getSaveFileName(self,'Simpan File',os.curdir,
        'Python Code (*.py);; PHP Code (*.php)','*.py')
        if not filename[0]: return
        self.label.setText('Nama File: ' + filename[0])
        fileHandle = QFile(filename[0])
        if not fileHandle.open(QIODevice.WriteOnly): return
        stream = QTextStream(fileHandle)
        stream << self.textEdit.document().toPlainText()
        stream.flush()
        fileHandle.close()

if __name__ == "__main__":
    a = QApplication(sys.argv)
    form = MainForm()
    form.show()
    a.exec_() 