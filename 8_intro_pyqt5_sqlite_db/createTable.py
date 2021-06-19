import sys
from PyQt5.QtSql import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


def connectdb():
    db = QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('db2.db')
    if db.open():
        print("koneksi berhasil di buat")
    else:
        print('ERROR: ' + db.lastError().text())

    query = QSqlQuery()
    sql = '''
        CREATE TABLE phonebooks (
            id INTEGER NOT NULL PRIMARY KEY,
            nama VARCHAR(25),
            nohp VARCHAR(15)
        ) '''

    query.exec_(sql)
    # return True

    print(db.tables())

""" if __name__ == '__main__':
    app = QApplication(sys.argv)
    connectdb() """
