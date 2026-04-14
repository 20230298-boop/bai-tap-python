import sys
from PyQt6.QtWidgets import *
from register_ui import Ui_Form
from list_ui import Ui_MainWindow
from database import *

# ================= REGISTER =================
class RegisterForm(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.id_edit = None  # dùng để phân biệt thêm hay sửa

        self.load_combo()
        self.ui.btnDangKy.clicked.connect(self.dang_ky)

    def load_combo(self):
        for i in range(1, 32):
            self.ui.cbNgay.addItem(str(i))
        for i in range(1, 13):
            self.ui.cbThang.addItem(f"Tháng {i}")
        for i in range(1970, 2025):
            self.ui.cbNam.addItem(str(i))

    def dang_ky(self):
        ho = self.ui.txtHo.text()
        ten = self.ui.txtTen.text()
        email = self.ui.txtEmail.text()
        password = self.ui.txtPassword.text()

        ngay_sinh = f"{self.ui.cbNgay.currentText()}/{self.ui.cbThang.currentText()}/{self.ui.cbNam.currentText()}"
        gioi_tinh = "Nam" if self.ui.radNam.isChecked() else "Nữ"

        # VALIDATE
        if not all([ho, ten, email, password]):
            QMessageBox.warning(self, "Lỗi", "Nhập đầy đủ thông tin")
            return

        if len(password) < 8:
            QMessageBox.warning(self, "Lỗi", "Mật khẩu >= 8 ký tự")
            return

        if not self.ui.chkDongY.isChecked():
            QMessageBox.warning(self, "Lỗi", "Chưa đồng ý điều khoản")
            return

        conn = connect_db()
        cursor = conn.cursor()

        if self.id_edit is None:
            # ===== INSERT =====
            cursor.execute("""
            INSERT INTO members (ho, ten, email, password, ngay_sinh, gioi_tinh)
            VALUES (?, ?, ?, ?, ?, ?)
            """, (ho, ten, email, password, ngay_sinh, gioi_tinh))
        else:
            # ===== UPDATE =====
            cursor.execute("""
            UPDATE members
            SET ho=?, ten=?, email=?, password=?, ngay_sinh=?, gioi_tinh=?
            WHERE id=?
            """, (ho, ten, email, password, ngay_sinh, gioi_tinh, self.id_edit))

        conn.commit()
        conn.close()

        QMessageBox.information(self, "OK", "Lưu thành công")

        # quay lại danh sách
        self.list = ListForm()
        self.list.show()
        self.close()


# ================= LIST =================
class ListForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.load_data()

        self.ui.btnXoa.clicked.connect(self.xoa)
        self.ui.btnSua.clicked.connect(self.sua)

    def load_data(self):
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM members")
        data = cursor.fetchall()

        self.ui.tableMember.setRowCount(len(data))
        self.ui.tableMember.setColumnCount(7)
        self.ui.tableMember.setHorizontalHeaderLabels(
            ["ID", "Họ", "Tên", "Email", "Mật khẩu", "Ngày sinh", "Giới tính"]
        )

        for i, row in enumerate(data):
            for j, val in enumerate(row):
                self.ui.tableMember.setItem(i, j, QTableWidgetItem(str(val)))

        conn.close()

    def xoa(self):
        row = self.ui.tableMember.currentRow()
        if row == -1:
            QMessageBox.warning(self, "Lỗi", "Chọn dòng để xóa")
            return

        id = self.ui.tableMember.item(row, 0).text()

        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM members WHERE id=?", (id,))
        conn.commit()
        conn.close()

        self.load_data()

    def sua(self):
        row = self.ui.tableMember.currentRow()
        if row == -1:
            QMessageBox.warning(self, "Lỗi", "Chọn dòng để sửa")
            return

        # lấy dữ liệu
        id = self.ui.tableMember.item(row, 0).text()
        ho = self.ui.tableMember.item(row, 1).text()
        ten = self.ui.tableMember.item(row, 2).text()
        email = self.ui.tableMember.item(row, 3).text()
        password = self.ui.tableMember.item(row, 4).text()

        # mở form đăng ký
        self.form = RegisterForm()

        # truyền dữ liệu sang
        self.form.ui.txtHo.setText(ho)
        self.form.ui.txtTen.setText(ten)
        self.form.ui.txtEmail.setText(email)
        self.form.ui.txtPassword.setText(password)

        self.form.id_edit = id  # gán id để update

        self.form.show()
        self.close()


# ================= MAIN =================
if __name__ == "__main__":
    create_table()

    app = QApplication(sys.argv)

    window = RegisterForm()
    window.show()

    sys.exit(app.exec())