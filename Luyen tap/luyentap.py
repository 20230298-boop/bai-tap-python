import math

# 1. Tính tổng 2 số
def tong_2_so(a, b):
    return a + b

# 2. Tính tổng các số trong danh sách
def tong_danh_sach(ds):
    return sum(ds)

# 3. Kiểm tra số nguyên tố
def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# 4. Tìm số nguyên tố trong đoạn [a, b]
def tim_so_nguyen_to(a, b):
    return [i for i in range(a, b + 1) if la_so_nguyen_to(i)]

# 5. Kiểm tra số hoàn hảo
def la_so_hoan_hao(n):
    if n <= 0:
        return False
    tong = sum(i for i in range(1, n) if n % i == 0)
    return tong == n

# 6. Tìm số hoàn hảo trong đoạn [a, b]
def tim_so_hoan_hao(a, b):
    return [i for i in range(a, b + 1) if la_so_hoan_hao(i)]

# MENU
def menu():
    while True:
        print("\n===== MENU =====")
        print("1. Tính tổng 2 số")
        print("2. Tính tổng danh sách số")
        print("3. Kiểm tra số nguyên tố")
        print("4. Tìm số nguyên tố trong đoạn [a, b]")
        print("5. Kiểm tra số hoàn hảo")
        print("6. Tìm số hoàn hảo trong đoạn [a, b]")
        print("0. Thoát")

        chon = input("Chọn chức năng: ")

        if chon == "1":
            a = float(input("Nhập a: "))
            b = float(input("Nhập b: "))
            print("Tổng =", tong_2_so(a, b))

        elif chon == "2":
            ds = list(map(int, input("Nhập các số cách nhau bởi dấu cách: ").split()))
            print("Tổng =", tong_danh_sach(ds))

        elif chon == "3":
            n = int(input("Nhập n: "))
            print("Là số nguyên tố" if la_so_nguyen_to(n) else "Không phải số nguyên tố")

        elif chon == "4":
            a = int(input("Nhập a: "))
            b = int(input("Nhập b: "))
            print("Các số nguyên tố:", tim_so_nguyen_to(a, b))

        elif chon == "5":
            n = int(input("Nhập n: "))
            print("Là số hoàn hảo" if la_so_hoan_hao(n) else "Không phải số hoàn hảo")

        elif chon == "6":
            a = int(input("Nhập a: "))
            b = int(input("Nhập b: "))
            print("Các số hoàn hảo:", tim_so_hoan_hao(a, b))

        elif chon == "0":
            print("Thoát chương trình!")
            break

        else:
            print("Lựa chọn không hợp lệ!")

# Chạy chương trình
menu()