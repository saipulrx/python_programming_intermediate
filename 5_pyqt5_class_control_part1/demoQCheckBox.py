import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi

class MainForm(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self,parent)
        # load file .ui yg dibuat di qt designer
        loadUi("/Users/muhammadsaipulrohman/Documents/IDB/source_code/qtDesigner/demo_qcheckbox.ui",self)

        self.btnOK.clicked.connect(self.btnOKClick)
        self.btnKeluar.clicked.connect(self.close)

    def btnOKClick(self):
        choices = []
        if self.cbPython.isChecked(): choices.append('Python')
        if self.cbJava.isChecked(): choices.append('Java')
        if self.cbPHP.isChecked(): choices.append('PHP')
        if self.cbCsharp.isChecked(): choices.append('C#')
        QMessageBox.information(self,'Informasi',repr(choices))

if __name__ == "__main__":
    a = QApplication(sys.argv)
    form = MainForm()
    form.show()
    a.exec_() 