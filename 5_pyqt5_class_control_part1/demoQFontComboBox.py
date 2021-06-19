import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUi

class MainForm(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self,parent)
        # load file .ui yg dibuat di qt designer
        loadUi("/Users/muhammadsaipulrohman/Documents/IDB/source_code/qtDesigner/demoQFontComboBox.ui",self)

        self.fontComboBox.activated.connect(self.fontComboBoxActivated)

    def fontComboBoxActivated(self):
        self.lineEdit.setFont(
            QFont(self.fontComboBox.currentText(),15)
        )

if __name__ == "__main__":
    a = QApplication(sys.argv)
    form = MainForm()
    form.show()
    a.exec_() 