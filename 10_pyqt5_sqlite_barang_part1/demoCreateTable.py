import sys, sqlite3
from sqlite3 import Error
from PyQt5.QtSql import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUi

tableDefinition=""

class MainForm(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self,parent)
        # load file .ui yg dibuat di qt designer
        loadUi("/Users/muhammadsaipulrohman/Documents/IDB/source_code/qtDesigner/demoCreateTable.ui",self)

        self.pushButtonAddColumn.clicked.connect(self.AddColumn)
        self.pushButtonCreateTable.clicked.connect(self.CreateTable)

    def AddColumn(self):
        global tableDefinition 
        if tableDefinition=="":
            tableDefinition="CREATE TABLE IF NOT EXISTS " + self.lineEditTableName.text()+" (" + self.lineEditColumnName.text()+" " + self.comboBoxDataType.itemText(self.comboBoxDataType.currentIndex())
            self.lineEditColumnName.setText("")
            self.lineEditColumnName.setFocus()
        else:
            tableDefinition+=","+self.lineEditColumnName.text()+ " " + self.comboBoxDataType.itemText(self.comboBoxDataType.currentIndex())
            self.lineEditColumnName.setText("")
            self.lineEditColumnName.setFocus()

    def CreateTable(self):
        global tableDefinition
        try:
            conn = sqlite3.connect(self.lineEditDBName.text()+".db")
            dbName = self.lineEditDBName.text()
            tableName = self.lineEditTableName.text()
            self.labelResponse.setText("Database %s is connected " %dbName)
            c = conn.cursor()
            tableDefinition+=");"
            c.execute(tableDefinition) 
            self.labelResponse.setText("Table %s is successfully created" %tableName)
        except Error as e:
            self.labelResponse.setText("Error in creating table")
        finally:
            conn.close()

if __name__=="__main__":
    app = QApplication(sys.argv) 
    w = MainForm()
    w.show() 
    sys.exit(app.exec_())  
