import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi

class MainForm(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self,parent)
        # load file .ui yg dibuat di qt designer
        loadUi("/Users/muhammadsaipulrohman/Documents/IDB/source_code/qtDesigner/demoQComboBox.ui",self)

        self.pushButton.clicked.connect(self.getTextButtonClick)

    def getTextButtonClick(self):
        if self.comboBox.currentText() == '-- Pilih Agama --':
            QMessageBox.critical(self,'Kesalahan','Harap memilih agama yang tersedia')
        else:    
            QMessageBox.information(self,'Informasi','Anda memilih: ' + self.comboBox.currentText())

if __name__ == "__main__":
    a = QApplication(sys.argv)
    form = MainForm()
    form.show()
    a.exec_() 