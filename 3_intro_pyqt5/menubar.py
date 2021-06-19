import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class menuDemo(QWidget):
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
      actionFile.addAction("Quit")

      #add Menu Edit
      actionEdit = menubar.addMenu("Edit")
      actionEdit.addAction("Cut Ctrl+X")
      actionEdit.addAction("Copy Ctrl+C")
      actionEdit.addAction("Paste Ctrl+V")
      actionEdit.addSeparator()
      actionEdit.addAction("Undo Ctrl+Z")
      actionEdit.addAction("Redo Ctrl+Y")

    # add textbox
      tbox = QPlainTextEdit()
      layout.addWidget(tbox, 1, 0)

app = QApplication(sys.argv)
screen = menuDemo()
screen.show()
sys.exit(app.exec_())