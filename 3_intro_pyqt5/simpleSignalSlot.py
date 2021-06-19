import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class dialog(QWidget):
    def __init__(self):
      QWidget.__init__(self)
      layout = QGridLayout()
      self.setLayout(layout)

      #create menu
      menubar = QMenuBar()
      layout.addWidget(menubar,0,0)

      #add Menu File
      actionFile = menubar.addMenu("File")
      actionFile.addAction("New")
      actionFile.addAction("Open")
      actionFile.addAction("Save")
      actionFile.addSeparator()
      actionFile.addAction("Keluar ")
    
    def aksiKeluar():
        mbox = QMessageBox()
        mbox.setText("Apakah Anda Ingin Keluar dari aplikasi ?")
        mbox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            
        mbox.exec_()

app = QApplication(sys.argv)
screen = menuDemo()
screen.show()
sys.exit(app.exec_())
