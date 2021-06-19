import sys
import calendar
from PyQt5.QtWidgets import QApplication, QWidget, QCalendarWidget, QLabel
from PyQt5.QtCore import QDate

class Example(QWidget):

   def __init__(self):
      super(Example, self).__init__()

      self.initUI()
		
   def initUI(self):
      cal = QCalendarWidget(self)
      cal.setGridVisible(True)
      cal.move(20, 20)
      cal.clicked[QDate].connect(self.showDate)
		
      self.lbl = QLabel(self)
      date = cal.selectedDate()
      self.lbl.setText(date.toString())
      self.lbl.move(20, 200)
      self.lbl.resize(300,300)
		
      self.setGeometry(100,100,400,400)
      self.setWindowTitle('Calendar')
      self.show()
		
   def showDate(self, date):
      self.lbl.setText(date.toString())
		
def main():
   app = QApplication(sys.argv)
   ex = Example()
   sys.exit(app.exec_())
	
if __name__ == '__main__':
   main()