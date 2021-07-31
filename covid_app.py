from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QWidget, \
    QVBoxLayout, QTableWidgetItem, QTableWidget
from PyQt5.QtGui import QIcon, QFont
import sys
from covid19_India_data import covid19


class Window(QWidget):
    def __init__(self):
        super().__init__()


        self.setGeometry(300,100,1015,800)
        self.setWindowTitle("Covid-19 All India Data")
        self.setWindowIcon(QIcon("covid.png"))


    def create_tables(self):
        vbox = QVBoxLayout()

        table_widget = QTableWidget()
        table_widget.setRowCount(36)
        table_widget.setColumnCount(6)

        data = covid19().covid_data()
        columns = list(data.columns)

        table_widget.setHorizontalHeaderLabels(columns)
        stylesheet = "::section{Background-color:rgb(0,0,0);color:white;border-radius:14px;}"
        table_widget.horizontalHeader().setStyleSheet(stylesheet)
        table_widget.verticalHeader().setStyleSheet(stylesheet)
        table_widget.horizontalHeader().setFont(QFont("times new roman", 12))
        table_widget.verticalHeader().setFont(QFont("times new roman", 12))

        header = table_widget.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)


        for row in range(len(data.index)):
            for col in range(len(data.columns)):
                table_widget.setItem(row, col, QTableWidgetItem(data.iloc[row,col]))
                if row % 2 == 0:
                    table_widget.item(row,col).setBackground(QtGui.QColor(190,190,190))
                else:
                    table_widget.item(row, col).setBackground(QtGui.QColor(224, 224, 224))
        vbox.addWidget(table_widget)


        self.setLayout(vbox)



if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Window()

    window.create_tables()
    window.show()


    sys.exit(App.exec())