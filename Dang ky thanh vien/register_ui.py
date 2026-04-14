from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 500)

        self.txtHo = QtWidgets.QLineEdit(Form)
        self.txtHo.setGeometry(QtCore.QRect(30, 60, 150, 30))
        self.txtHo.setPlaceholderText("Họ")

        self.txtTen = QtWidgets.QLineEdit(Form)
        self.txtTen.setGeometry(QtCore.QRect(200, 60, 150, 30))
        self.txtTen.setPlaceholderText("Tên")

        self.txtEmail = QtWidgets.QLineEdit(Form)
        self.txtEmail.setGeometry(QtCore.QRect(30, 110, 320, 30))
        self.txtEmail.setPlaceholderText("Email")

        self.txtPassword = QtWidgets.QLineEdit(Form)
        self.txtPassword.setGeometry(QtCore.QRect(30, 160, 320, 30))
        self.txtPassword.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.txtPassword.setPlaceholderText("Mật khẩu")

        self.cbNgay = QtWidgets.QComboBox(Form)
        self.cbNgay.setGeometry(QtCore.QRect(30, 220, 80, 25))

        self.cbThang = QtWidgets.QComboBox(Form)
        self.cbThang.setGeometry(QtCore.QRect(130, 220, 100, 25))

        self.cbNam = QtWidgets.QComboBox(Form)
        self.cbNam.setGeometry(QtCore.QRect(250, 220, 100, 25))

        self.radNam = QtWidgets.QRadioButton("Nam", Form)
        self.radNam.setGeometry(QtCore.QRect(30, 270, 80, 20))

        self.radNu = QtWidgets.QRadioButton("Nữ", Form)
        self.radNu.setGeometry(QtCore.QRect(120, 270, 80, 20))

        self.chkDongY = QtWidgets.QCheckBox("Tôi đồng ý điều khoản", Form)
        self.chkDongY.setGeometry(QtCore.QRect(30, 310, 250, 30))

        self.btnDangKy = QtWidgets.QPushButton("Đăng ký", Form)
        self.btnDangKy.setGeometry(QtCore.QRect(130, 370, 120, 35))

        self.label = QtWidgets.QLabel("Đăng ký", Form)
        self.label.setGeometry(QtCore.QRect(150, 10, 120, 30))

        QtCore.QMetaObject.connectSlotsByName(Form)