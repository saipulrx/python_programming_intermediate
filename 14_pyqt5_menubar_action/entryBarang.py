import sys
from PyQt5.QtSql import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUi

class EntryBarang(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self,parent)
        # load file .ui yg dibuat di qt designer
        loadUi("/Users/muhammadsaipulrohman/Documents/IDB/source_code/qtDesigner/entryBarang.ui",self)

        self.mode = -1 # 0: mode tambah, 1: mode ubah

        if self.mode == 0:
            self.txtNamaBarang.clear()
            self.txtHarga.clear()
            self.stock.setValue(0)

        self.btnOK.clicked.connect(self.accept)
        self.btnBatal.clicked.connect(self.reject)