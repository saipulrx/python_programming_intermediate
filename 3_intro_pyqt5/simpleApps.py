import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(300,300)
    w.setWindowTitle('Simple Apps using PyQt5')

    # Set window background color
    w.setAutoFillBackground(True)
    color = w.palette()
    color.setColor(w.backgroundRole(), Qt.darkBlue)
    w.setPalette(color)
    
    w.show()
    sys.exit(app.exec_())