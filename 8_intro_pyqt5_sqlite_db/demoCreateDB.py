import sys
from PyQt5.QtSql import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUi

class MainForm(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self,parent)
        # load file .ui yg dibuat di qt designer
        loadUi("/Users/muhammadsaipulrohman/Documents/IDB/source_code/qtDesigner/demoDB.ui",self)

        self.pushButtonCreateDB.clicked.connect(self.CreateDB)

    def CreateDB(self):
        db = QSqlDatabase.addDatabase('QSQLITE')
        dbName = self.lineEditDBName.text()+".db"
        db.setDatabaseName(dbName)
        if db.open():
            self.labelResponse.setText("Database %s is created " %dbName)
        else:
            self.labelResponse.setText("Some error has occured ")

if __name__=="__main__":
    app = QApplication(sys.argv) 
    w = MainForm()
    w.show() 
    sys.exit(app.exec_())  
