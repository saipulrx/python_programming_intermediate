import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi

class MainForm(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self,parent)
        # load file .ui yg dibuat di qt designer
        loadUi("/Users/muhammadsaipulrohman/Documents/IDB/source_code/qtDesigner/modul5_1.ui",self)
        
        # tambahkan aksi jika klik button Tambah maka akan memanggil ke fungsi btnTambahClick
        self.btnTambah.clicked.connect(self.btnTambahClick)
        # tambahkan aksi jika klik button Kurang maka akan memanggil ke fungsi btnKurangClick
        self.btnKurang.clicked.connect(self.btnKurangClick)
        # tambahkan aksi jika klik button Kali maka akan memanggil ke fungsi btnKaliClick
        self.btnKali.clicked.connect(self.btnKaliClick)
        # tambahkan aksi jika klik button Bagi maka akan memanggil ke fungsi btnBagiClick
        self.btnBagi.clicked.connect(self.btnBagiClick)
        # tambahkan aksi jika klik button Keluar maka akan memanggil ke fungsi btnKeluarClick 
        self.btnKeluar.clicked.connect(self.btnKeluarClick)

    # fungsi menghitung menggunakan operator aritmatika
    def calculate(self, operator):
        bil1 = float(self.txtBilangan1.text())
        bil2 = float(self.txtBilangan2.text())

        if operator == '+':
            hasil = bil1 + bil2 
        elif operator == '-':
            hasil = bil1 - bil2
        elif operator == '*':
            hasil = bil1 * bil2
        elif operator == '/':
            hasil = bil1 / bil2
        else:
            QMessageBox.critical(self,'Invalid Operation','Operasi yang anda masukkan salah')
        self.txtHasilHitung.setText(str(hasil))                

    # fungsi untuk operator tambah
    def btnTambahClick(self):
        self.calculate('+')

    # fungsi untuk operator kurang
    def btnKurangClick(self):
        self.calculate('-')

    # fungsi untuk operator kali
    def btnKaliClick(self):
        self.calculate('*')

    # fungsi untuk operator bagi
    def btnBagiClick(self):
        self.calculate('/')

    # fungsi ketika mengklik tombol keluar
    def btnKeluarClick(self):
        QApplication.quit()

if __name__ == "__main__":
    a = QApplication(sys.argv)
    form = MainForm()
    form.show()
    a.exec_()    
        