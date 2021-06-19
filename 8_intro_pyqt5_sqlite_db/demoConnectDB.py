import sys, sqlite3
from sqlite3 import Error
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
        try:
            conn = sqlite3.connect(self.lineEditDBName.text()+".db")
            dbName = self.lineEditDBName.text()
            self.labelResponse.setText("Database %s is created " %dbName)
        except Error as e:
            self.labelResponse.setText("Some error has occured ")
        finally:
            conn.close()

if __name__=="__main__":
    app = QApplication(sys.argv) 
    w = MainForm()
    w.show() 
    sys.exit(app.exec_())    




