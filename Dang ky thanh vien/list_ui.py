from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 400)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        MainWindow.setCentralWidget(self.centralwidget)

        self.tableMember = QtWidgets.QTableWidget(self.centralwidget)
        self.tableMember.setGeometry(QtCore.QRect(20, 20, 560, 250))

        self.btnXoa = QtWidgets.QPushButton("Xóa", self.centralwidget)
        self.btnXoa.setGeometry(QtCore.QRect(150, 300, 100, 30))

        self.btnSua = QtWidgets.QPushButton("Sửa", self.centralwidget)
        self.btnSua.setGeometry(QtCore.QRect(300, 300, 100, 30))

        QtCore.QMetaObject.connectSlotsByName(MainWindow)