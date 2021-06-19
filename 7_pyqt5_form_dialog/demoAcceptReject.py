import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUi

class DialogForm(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self,parent)
        # load file .ui yg dibuat di qt designer
        loadUi("/Users/muhammadsaipulrohman/Documents/IDB/source_code/qtDesigner/demoAcceptReject.ui",self)

        self.okButton.clicked.connect(self.accept)
        self.rejectButton.clicked.connect(self.reject)


class MainForm(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self,parent)
        # load file .ui yg dibuat di qt designer
        loadUi("/Users/muhammadsaipulrohman/Documents/IDB/source_code/qtDesigner/AcceptReject.ui",self)

        self.pushButton.clicked.connect(self.showDialogButtonClick)

    def showDialogButtonClick(self):
        form = DialogForm()
        if form.exec_() == QDialog.Accepted:
            QMessageBox.information(self,'Informasi','Anda Memilih tombol OK')
        else: # QDialog.Rejected
            QMessageBox.information(self,'Informasi','Anda memilih tombol Batal')

if __name__ == "__main__":
    a = QApplication(sys.argv)
    form = MainForm()
    form.show()
    a.exec_() 