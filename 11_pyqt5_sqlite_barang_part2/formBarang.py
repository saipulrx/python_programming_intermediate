import sys
from PyQt5.QtSql import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUi
from entryBarang import *

class MainForm(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self,parent)
        # load file .ui yg dibuat di qt designer
        loadUi("/Users/muhammadsaipulrohman/Documents/IDB/source_code/qtDesigner/formDataBarang.ui",self)
        self.btnAdd.clicked.connect(self.addButton)
        self.btnEdit.clicked.connect(self.editButton)
        self.btnDelete.clicked.connect(self.deleteButton)

        self.loadData()

    def loadData(self):
        self.table.clear()
        self.table.setRowCount(self.getRowCount())
        self.table.setColumnCount(4)
        columnHeaders = ['ID','Nama Barang','Harga','Stock']
        self.table.setHorizontalHeaderLabels(columnHeaders)

        query = QSqlQuery()
        ID, NAMABARANG, HARGA, STOCK = range(4)
        row = 0
        query.exec_('SELECT * FROM barang')
        while query.next():
            for i in range(4):
                item = QTableWidgetItem()
                item.setText(str(query.value(i)))
                self.table.setItem(row, i, item)
            row += 1
        
        self.table.resizeColumnsToContents()
        self.table.resizeRowsToContents()

    def getRowCount(self):
        query = QSqlQuery()
        query.exec_('SELECT COUNT(*) FROM barang')
        query.next()
        rowCount = query.value(0)
        return rowCount

    def addButton(self):
        self.entryBarang = EntryBarang()
        self.mode = 0
        if self.entryBarang.exec_() == QDialog.Accepted:
            id = self.getRowCount() + 1
            query = QSqlQuery()
            query.exec_("INSERT INTO barang VALUES (%d, '%s', '%s',%d)" % 
            (id, self.entryBarang.txtNamaBarang.text(), self.entryBarang.txtHarga.text(),self.entryBarang.stock.value()))
            self.loadData()

    def editButton(self):
        self.entryBarang = EntryBarang()
        self.mode = 1
        self.entryBarang.txtNamaBarang.setText(
            self.table.item(self.table.currentRow(), 1).text()
        )
        self.entryBarang.txtHarga.setText(
            self.table.item(self.table.currentRow(), 2).text()
        )
        self.entryBarang.stock.setValue(
            int(self.table.item(self.table.currentRow(),3).text())
        )

        if self.entryBarang.exec_() == QDialog.Accepted:
            id = int(self.table.item(self.table.currentRow(), 0).text())
            query = QSqlQuery()
            query.exec_(
                '''UPDATE barang
                    SET nama_barang = '%s', harga = '%s', stock = %d
                    WHERE id = %d
                ''' % (self.entryBarang.txtNamaBarang.text(),
                self.entryBarang.txtHarga.text(), self.entryBarang.stock.value(), id)
            )
            self.loadData()

    def deleteButton(self):
        id = int(self.table.item(self.table.currentRow(), 0).text())
        query = QSqlQuery()
        query.exec_(
            'DELETE FROM barang WHERE id = %d' % id
        )
        self.loadData()


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