import sys
from PyQt5.QtSql import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUi

class MainForm(QWidget):

    recordNumber = 0

    def __init__(self, parent=None):
        QWidget.__init__(self,parent)
        # load file .ui yg dibuat di qt designer
        loadUi("/Users/muhammadsaipulrohman/Documents/IDB/source_code/qtDesigner/formNavigasiDataBarang.ui",self)

        #define variable model menggunakan QSqlTableModel()
        self.model = QSqlTableModel()
        #define tabel lalu dimasukan di variable model
        self.model.setTable('barang')
        #untuk mengubah data bisa langsung di table view
        self.model.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.model.select()

        self.firstButtonClick()

        self.firstButton.clicked.connect(self.firstButtonClick)
        self.prevButton.clicked.connect(self.prevButtonClick)
        self.nextButton.clicked.connect(self.nextButtonClick)
        self.lastButton.clicked.connect(self.lastButtonClick)

    def setData(self):
        record = self.model.record(MainForm.recordNumber)
        self.txtNamaBarang.setText(str(record.value('nama_barang')))
        self.txtHarga.setText(str(record.value('harga')))
        self.txtStock.setText(str(record.value('stock')))

    def firstButtonClick(self):
        MainForm.recordNumber = 0
        self.setData()

    def prevButtonClick(self):
        if MainForm.recordNumber == 0: return
        MainForm.recordNumber -= 1
        self.setData()
    
    def nextButtonClick(self):
        if MainForm.recordNumber == self.model.rowCount()-1: return
        MainForm.recordNumber +=1
        self.setData()

    def lastButtonClick(self):
        MainForm.recordNumber = self.model.rowCount()-1
        self.setData()

if __name__=="__main__":
    app = QApplication(sys.argv) 

    db = QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('barang.db')

    if not db.open():
        print('ERROR: ' + db.lastError().text())
        sys.exit(1)
    
    form = MainForm()
    form.show()

    app.exec_()    