# Bài 3
a = int(input("Nhap so a: "))
b = int(input("Nhap so b: "))
c = int(input("Nhap so c: "))

# a) Tổng và tích
tong = a + b + c
tich = a * b * c
print("Tong =", tong)
print("Tich =", tich)

# b) Hiệu của 2 số bất kỳ (ví dụ a - b)
print("Hieu a - b =", a - b)
print("Hieu b - c =", b - c)
print("Hieu a - c =", a - c)

# c) Chia 2 số bất kỳ (ví dụ a chia b)
if b != 0:
    print("Chia a cho b:")
    print("Phan nguyen =", a // b)
    print("Phan du =", a % b)
    print("Ket qua chinh xac =", a / b)
else:
    print("Khong the chia cho 0")