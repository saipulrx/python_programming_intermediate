import sys
from PyQt5.QtSql import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUi
from entryData import *

class MainForm(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self,parent)
        # load file .ui yg dibuat di qt designer
        loadUi("/Users/muhammadsaipulrohman/Documents/IDB/source_code/qtDesigner/loadData.ui",self)
        self.btnAdd.clicked.connect(self.addButton)
        self.btnEdit.clicked.connect(self.editButton)
        self.btnDelete.clicked.connect(self.deleteButton)

        self.loadData()

    def loadData(self):
        self.table.clear()
        self.table.setRowCount(self.getRowCount())
        self.table.setColumnCount(3)
        columnHeaders = ['ID','Nama','No HP']
        self.table.setHorizontalHeaderLabels(columnHeaders)

        query = QSqlQuery()
        ID, NAMA, NOHP = range(3)
        row = 0
        query.exec_('SELECT * FROM kontak')
        while query.next():
            for i in range(3):
                item = QTableWidgetItem()
                item.setText(str(query.value(i)))
                self.table.setItem(row, i, item)
            row += 1
    
        self.table.resizeColumnsToContents()
        self.table.resizeRowsToContents()
        
    def getRowCount(self):
        query = QSqlQuery()
        query.exec_('SELECT COUNT(*) FROM kontak')
        query.next()
        rowCount = query.value(0)
        return rowCount

    def addButton(self):
        self.entryForm = EntryForm()
        self.mode = 0
        if self.entryForm.exec_() == QDialog.Accepted:
            id = self.getRowCount() + 1
            query = QSqlQuery()
            query.exec_("INSERT INTO kontak VALUES (%d, '%s', '%s')" % 
            (id, self.entryForm.txtName.text(), self.entryForm.txtPhone.text()))
            self.loadData()

    def editButton(self):
        self.entryForm = EntryForm()
        self.mode = 1
        self.entryForm.txtName.setText(
            self.table.item(self.table.currentRow(), 1).text()
        )
        self.entryForm.txtPhone.setText(
            self.table.item(self.table.currentRow(), 2).text()
        )
        if self.entryForm.exec_() == QDialog.Accepted:
            id = int(self.table.item(self.table.currentRow(), 0).text())
            query = QSqlQuery()
            query.exec_(
                '''UPDATE kontak
                    SET nama = '%s', nohp = '%s'
                    WHERE id = %d
                ''' % (self.entryForm.txtName.text(),
                self.entryForm.txtPhone.text(), id)
            )
            self.loadData()

    def deleteButton(self):
        id = int(self.table.item(self.table.currentRow(), 0).text())
        query = QSqlQuery()
        query.exec_(
            'DELETE FROM kontak WHERE id = %d' % id
        )
        self.loadData()


if __name__=="__main__":
    app = QApplication(sys.argv) 

    db = QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('kontak.db')

    if not db.open():
        print('ERROR: ' + db.lastError().text())
        sys.exit(1)
    
    form = MainForm()
    form.show()

    app.exec_()


