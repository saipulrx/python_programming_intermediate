import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUi

class MainForm(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self,parent)
        # load file .ui yg dibuat di qt designer
        loadUi("/Users/muhammadsaipulrohman/Documents/IDB/source_code/qtDesigner/demoMetodeQMessageBox.ui",self)

        self.aboutButton.clicked.connect(self.aboutButtonClick)
        self.criticalButton.clicked.connect(self.criticalButtonClick)
        self.informationButton.clicked.connect(self.informationButtonClick)
        self.questionButton.clicked.connect(self.questionButtonClick)
        self.warningButton.clicked.connect(self.warningButtonClick)

    def aboutButtonClick(self):
        QMessageBox.about(self,'Tentang Program','Sample QMessageBox')

    def criticalButtonClick(self):
        QMessageBox.critical(self,'Kesalahan','file setting.conf tidak ditemukan')

    def informationButtonClick(self):
        QMessageBox.information(self,'Informasi','Proses upload file telah berhasil')

    def questionButtonClick(self):
        filename = 'settings.conf'
        response = QMessageBox.question(self,'Konfirmasi','Anda yakin akan menghapus file %s?' %filename)

        if response == QMessageBox.Yes:
            QMessageBox.about(self,'Respon','Anda memilih Tombol Yes')
        else:
            QMessageBox.about(self,'Respon','Anda memilih Tombol No')

    def warningButtonClick(self):
        QMessageBox.warning(self,'Peringatan','Operasi ini akan menghapus semua data di dalam disk anda')

if __name__ == "__main__":
    a = QApplication(sys.argv)
    form = MainForm()
    form.show()
    a.exec_()   

