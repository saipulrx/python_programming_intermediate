import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUi

class DialogForm(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self,parent)
        # load file .ui yg dibuat di qt designer
        loadUi("/Users/muhammadsaipulrohman/Documents/IDB/source_code/qtDesigner/demoDialogModal.ui",self)

        self.closeButton.clicked.connect(self.close)

class MainForm(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self,parent)
        # load file .ui yg dibuat di qt designer
        loadUi("/Users/muhammadsaipulrohman/Documents/IDB/source_code/qtDesigner/dialogSetModal.ui",self)

        self.modalButton.clicked.connect(self.showModalDialog)
        self.nonModalButton.clicked.connect(self.showNonModalDialog)

    def showModalDialog(self):
        self.form = DialogForm()
        self.form.label.setText('Dialog bersifat modal')
        self.form.setModal(True)
        self.form.show()

    def showNonModalDialog(self):
        self.form = DialogForm()
        self.form.label.setText('Dialog bersifat non-modal')
        self.form.setModal(False)
        self.form.show()

if __name__ == "__main__":
    a = QApplication(sys.argv)
    form = MainForm()
    form.show()
    a.exec_()    