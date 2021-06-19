import sys
from PyQt5.QtSql import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUi
from formBuku import FormDataBuku
from formBarang import FormDataBarang
from navigasiDataBarang import FormNavigasiBarang
from demoCreateTables import FormCreateTables
from demoQTableWidget import FormQTableWidget

class MenuForm(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self,parent)
        # load file .ui yg dibuat di qt designer
        loadUi("/Users/muhammadsaipulrohman/Documents/IDB/source_code/qtDesigner/simpleMenubar.ui",self)
        self.actionForm_Data_Buku.triggered.connect(self.loadDataBuku)
        self.actionCRUD_Data_Barang.triggered.connect(self.loadDataBarang)
        self.actionNavigasi_Data_Barang.triggered.connect(self.loadNavigasiDataBarang)
        self.actionForm_Create_New_DB_Tables.triggered.connect(self.createDBTables)

        self.actionDemo_QTableWidget.triggered.connect(self.loadQTableWidget)

    def loadDataBuku(self):
        #connect to database library.db
        library_db = QSqlDatabase.addDatabase('QSQLITE')
        library_db.setDatabaseName('library.db')
        
        if not library_db.open():
            print('ERROR: ' + library_db.lastError().text())
            sys.exit(1)
        
        self.formDataBuku = FormDataBuku()
        self.formDataBuku.show()

    def loadDataBarang(self):
        #connect to database barang.db
        barang_db = QSqlDatabase.addDatabase('QSQLITE')
        barang_db.setDatabaseName('barang.db')
        if not barang_db.open():
            print('ERROR: ' + barang_db.lastError().text())
            sys.exit(1)

        self.formDataBarang = FormDataBarang()
        self.formDataBarang.show()

    def loadNavigasiDataBarang(self):
        #connect to database barang.db
        barang_db = QSqlDatabase.addDatabase('QSQLITE')
        barang_db.setDatabaseName('barang.db')
        if not barang_db.open():
            print('ERROR: ' + barang_db.lastError().text())
            sys.exit(1)

        self.formNavigasiDataBarang = FormNavigasiBarang()
        self.formNavigasiDataBarang.show()

    def createDBTables(self):
        self.formCreateDBTables = FormCreateTables()
        self.formCreateDBTables.show()

    def loadQTableWidget(self):
        self.formQTableWidget = FormQTableWidget()
        self.formQTableWidget.show()


if __name__=="__main__":
    app = QApplication(sys.argv) 
    form = MenuForm()

    form.show()
    app.exec_()