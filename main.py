import sys

from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
import sqlite3

if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)
        self.initUI()

    def initUI(self):
        con = sqlite3.connect("coffee.sqlite")
        cur = con.cursor()

        headers = ["сорт", "степень обжарки", "молотый/в зернах", "вкус", "цена(руб)", "объем(г)"]
        data = cur.execute("SELECT * FROM coffees").fetchall()
        self.coffeeTable.setRowCount(len(data))
        self.coffeeTable.setColumnCount(6)

        for h in range(6):
            header = QTableWidgetItem()
            header.setText(headers[h])
            self.coffeeTable.setHorizontalHeaderItem(h, header)

        for i in range(len(data)):
            for j in range(7):
                if j == 6:
                    item = QTableWidgetItem(str(data[i][j]))
                else:
                    item = QTableWidgetItem(str(data[i][j + 1]))
                self.coffeeTable.setItem(i, j, item)
        self.coffeeTable.resizeColumnsToContents()
        con.close()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Main()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())