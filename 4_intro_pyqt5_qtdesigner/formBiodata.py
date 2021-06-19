import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi

class MainForm(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self,parent)
        loadUi('/Users/muhammadsaipulrohman/Documents/IDB/source_code/qtDesigner/biodataLengkap.ui',self)
        self.btnSimpan.clicked.connect(self.btnSimpanClick)
        self.btnBatal.clicked.connect(self.btnBatalClick)

    def btnSimpanClick(self):
        self.listWidget.addItem(
            self.txtNama.text() + ' - ' + self.txtNomorHp.text() + 
            ' - ' + self.txtEmail.text() + ' - ' + self.txtAlamat.toPlainText() + ' - ' +
            self.txtJenKel.text()
        )

    def btnBatalClick(self):
        QApplication.quit()
        

if __name__ == "__main__":
    a = QApplication(sys.argv)
    form = MainForm()
    form.show()
    a.exec_()