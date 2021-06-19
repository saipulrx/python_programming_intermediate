import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUi

class MainForm(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self,parent)
        # load file .ui yg dibuat di qt designer
        loadUi("/Users/muhammadsaipulrohman/Documents/IDB/source_code/qtDesigner/demoQDateTimeEdit.ui",self)

        # set object control QDateEdit as current Date
        self.dateEdit.setDate(QDate.currentDate())

        # set object control QTimeEdit as current Time
        self.timeEdit.setTime(QTime.currentTime())

        # set object control QDateTimeEdit as current Date Time
        self.dateTimeEdit.setDateTime(QDateTime.currentDateTime())

        # after click OK Button, display MessageBox with value Date, Time and Date Time
        self.pushButton.clicked.connect(self.OKButtonClick)

    def OKButtonClick(self):
        QMessageBox.information(self,'Informasi Tanggal dan Waktu saat ini',
        'Date: ' + self.dateEdit.date().toString() + '\n' + 
        'Time: ' + self.timeEdit.time().toString() + '\n' +
        'DateTime: ' + self.dateTimeEdit.dateTime().toString() + '\n')

if __name__ == "__main__":
    a = QApplication(sys.argv)
    form = MainForm()
    form.show()
    a.exec_() 


