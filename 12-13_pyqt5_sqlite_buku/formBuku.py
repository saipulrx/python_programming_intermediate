import sys
from PyQt5.QtSql import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUi
from entryBuku import *

class MainForm(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self,parent)
        # load file .ui yg dibuat di qt designer
        loadUi("/Users/muhammadsaipulrohman/Documents/IDB/source_code/qtDesigner/formDataBuku.ui",self)
        self.btnAdd.clicked.connect(self.addButton)
        self.btnEdit.clicked.connect(self.editButton)
        self.btnDelete.clicked.connect(self.deleteButton)
        self.btnSearch.clicked.connect(self.searchData)
        self.loadData()

    def loadData(self):
        self.tableEditBuku.clear()
        self.tableEditBuku.setRowCount(self.getRowCount())
        self.tableEditBuku.setColumnCount(5)
        columnHeaders = ['ID','Judul Buku','Total Halaman','Harga', 'Stock']
        self.tableEditBuku.setHorizontalHeaderLabels(columnHeaders)

        query = QSqlQuery()
        ID, JUDULBUKU, TOTALHALAMAN, HARGA, STOCK = range(5)
        row = 0
        query.exec_('SELECT * FROM book')
        while query.next():
            for i in range(5):
                item = QTableWidgetItem()
                item.setText(str(query.value(i)))
                self.tableEditBuku.setItem(row, i, item)
            row += 1
        
        self.tableEditBuku.resizeColumnsToContents()
        self.tableEditBuku.resizeRowsToContents()

    def getRowCount(self):
        query = QSqlQuery()
        query.exec_('SELECT COUNT(*) FROM book')
        query.next()
        rowCount = query.value(0)
        return rowCount

    def getRowCounts(self):
        query = QSqlQuery()
        query.exec_(
            '''SELECT COUNT(*) FROM book
            WHERE judul LIKE '%%%s%%' AND total_halaman LIKE '%%%s%%'
            AND harga LIKE '%%%s%%'
            ''' % (self.txtJudulBukuDetail.text(),self.txtTTLHal.text(),
            self.txtHargaDetail.text())
            )
        query.next()
        rowCount = query.value(0)
        return rowCount

    def addButton(self):
        self.entryBuku = EntryBuku()
        self.mode = 0
        if self.entryBuku.exec_() == QDialog.Accepted:
            id = self.getRowCount() + 1
            query = QSqlQuery()
            query.exec_("INSERT INTO book VALUES (%d, '%s', '%s','%s', %d)" % 
            (id, self.entryBuku.txtJudulBuku.text(), self.entryBuku.txtTotalHal.text(), 
            self.entryBuku.txtHarga.text(),self.entryBuku.stock.value()))
            self.loadData()

    def editButton(self):
        self.entryBuku = EntryBuku()
        self.mode = 1
        self.entryBuku.txtJudulBuku.setText(
            self.tableEditBuku.item(self.tableEditBuku.currentRow(), 1).text()
        )
        self.entryBuku.txtTotalHal.setText(
            self.tableEditBuku.item(self.tableEditBuku.currentRow(), 2).text()
        )
        self.entryBuku.txtHarga.setText(
            self.tableEditBuku.item(self.tableEditBuku.currentRow(), 3).text()
        )
        self.entryBuku.stock.setValue(
            int(self.tableEditBuku.item(self.tableEditBuku.currentRow(),4).text())
        )

        if self.entryBuku.exec_() == QDialog.Accepted:
            id = int(self.tableEditBuku.item(self.tableEditBuku.currentRow(), 0).text())
            query = QSqlQuery()
            query.exec_(
                '''UPDATE book
                    SET judul = '%s', total_halaman = '%s', harga = '%s', stock = %d
                    WHERE id = %d
                ''' % (self.entryBuku.txtJudulBuku.text(),
                self.entryBuku.txtTotalHal.text(), self.entryBuku.txtHarga.text(), 
                self.entryBuku.stock.value(), id)
            )
            self.loadData()

    def deleteButton(self):
        id = int(self.tableEditBuku.item(self.tableEditBuku.currentRow(), 0).text())
        query = QSqlQuery()
        query.exec_(
            'DELETE FROM book WHERE id = %d' % id
        )
        self.loadData()

    def searchData(self):
        self.tableDetailBuku.setRowCount(self.getRowCounts())
        self.tableDetailBuku.setColumnCount(5)
        querySearchData = QSqlQuery()
        ID, JUDULBUKU, TOTALHALAMAN, HARGA, STOCK = range(5)
        row = 0
        judulBuku = self.txtJudulBukuDetail.text()
        totalHalaman = self.txtTTLHal.text()
        harga = self.txtHargaDetail.text()
        querySearchData.exec_(
            '''SELECT * FROM book 
            WHERE judul LIKE '%%%s%%' AND total_halaman LIKE '%%%s%%' 
            AND harga LIKE '%%%s%%'
            ''' % (judulBuku,totalHalaman,harga)
        )

        while querySearchData.next():
            for i in range(5):
                itemDetail = QTableWidgetItem()
                itemDetail.setText(str(querySearchData.value(i)))
                self.tableDetailBuku.setItem(row, i, itemDetail)
            row += 1
        
        self.tableDetailBuku.resizeColumnsToContents()
        self.tableDetailBuku.resizeRowsToContents()

if __name__=="__main__":
    app = QApplication(sys.argv) 

    db = QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('library.db')

    if not db.open():
        print('ERROR: ' + db.lastError().text())
        sys.exit(1)
    
    form = MainForm()
    form.show()

    app.exec_()