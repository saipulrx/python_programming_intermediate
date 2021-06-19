import sys
from PyQt5.QtWidgets import *

if __name__ == "__main__":

    app = QApplication([])
    w = QWidget()
    w.setWindowTitle("Musketeers")

    btn1 = QPushButton("Athos")
    btn2 = QPushButton("Porthos")
    btn3 = QPushButton("Aramis")

    hbox = QHBoxLayout(w)

    hbox.addWidget(btn1)
    hbox.addWidget(btn2)
    hbox.addWidget(btn3)

    w.show()

    sys.exit(app.exec_())