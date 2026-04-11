from models.manager import Manager
from models.developer import Developer
from models.intern import Intern
from services.company import Company
from utils.validators import *

company = Company()

def menu():
    while True:
        print("\n===== QUẢN LÝ NHÂN VIÊN =====")
        print("1. Thêm nhân viên")
        print("2. Hiển thị danh sách")
        print("3. Tìm nhân viên")
        print("4. Tổng lương")
        print("5. Top 3 lương")
        print("6. Đánh giá hiệu suất")
        print("7. Phân công dự án")
        print("8. Xem thành viên dự án")
        print("9. Top 10 nhiều dự án")
        print("10. Top 10 ít dự án")
        print("11. Cắt giảm nhân sự")
        print("0. Thoát")

        choice = input("Chọn: ")

        try:
            if choice == "1":
                emp_id = input("ID: ")
                name = input("Tên: ")
                age = int(input("Tuổi: "))
                validate_age(age)

                coefficient = float(input("Hệ số lương: "))
                validate_coefficient(coefficient)

                t = input("Loại (1.Manager 2.Dev 3.Intern): ")

                if t == "1":
                    emp = Manager(emp_id, name, age, coefficient)
                elif t == "2":
                    lang = input("Ngôn ngữ: ")
                    emp = Developer(emp_id, name, age, coefficient, lang)
                else:
                    emp = Intern(emp_id, name, age, coefficient)

                company.add_employee(emp)

            elif choice == "2":
                company.list_all()

            elif choice == "3":
                emp = company.find_by_id(input("Nhập ID: "))
                print(emp)

            elif choice == "4":
                print("Tổng lương:", company.total_salary())

            elif choice == "5":
                for e in company.top_3_salary():
                    print(e)

            elif choice == "6":
                emp = company.find_by_id(input("ID: "))
                score = int(input("Điểm: "))
                validate_score(score)
                emp.performance = score

            elif choice == "7":
                emp_id = input("ID nhân viên: ")
                project = input("Tên dự án: ")
                company.assign_project(emp_id, project)

            elif choice == "8":
                project = input("Tên dự án: ")
                members = company.get_project_members(project)
                for m in members:
                    print(m, "-", type(m).__name__)

            elif choice == "9":
                for e in company.top_10_most_projects():
                    print(e, "- số dự án:", len(e.projects))

            elif choice == "10":
                for e in company.top_10_least_projects():
                    print(e, "- số dự án:", len(e.projects))

            elif choice == "11":
                ids = input("Nhập ID cần xóa (cách nhau dấu phẩy): ").split(",")
                removed = company.remove_multiple_employees(ids)
                print("Đã xóa:", removed)

            elif choice == "0":
                break

        except Exception as e:
            print("Lỗi:", e)

if __name__ == "__main__":
    menu()