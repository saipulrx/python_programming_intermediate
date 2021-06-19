import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi

class MainForm(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self,parent)
        # load file .ui yg dibuat di qt designer
        loadUi("/Users/muhammadsaipulrohman/Documents/IDB/source_code/qtDesigner/demoQRadioButton.ui",self)

        self.rbTambah.clicked.connect(lambda: self.lblResult.setText('<b>Hasil Penjumlahan: </b>'))
        self.rbKurang.clicked.connect(lambda: self.lblResult.setText('<b>Hasil Pengurangan: </b>'))
        self.rbKali.clicked.connect(lambda: self.lblResult.setText('<b>Hasil Perkalian: </b>'))
        self.rbBagi.clicked.connect(lambda: self.lblResult.setText('<b>Hasil Pembagian: </b>'))
        self.btnHitung.clicked.connect(self.btnHitungClick)

    def btnHitungClick(self):
        bil1 = float(self.txtbil1.text())
        bil2 = float(self.txtbil2.text())

        if (self.rbTambah.isChecked()):
            result = bil1 + bil2
        elif (self.rbKurang.isChecked()):
            result = bil1 - bil2
        elif (self.rbKali.isChecked()):
            result = bil1 * bil2
        else:
            result = bil1 / bil2

        index = str(self.lblResult.text()).index(':')
        s = str(self.lblResult.text())[:index+1]
        self.lblResult.setText('%s %.2f %s' % (s, result, '</b>'))

if __name__ == "__main__":
    a = QApplication(sys.argv)
    form = MainForm()
    form.show()
    a.exec_()          