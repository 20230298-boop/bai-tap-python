# Nhập tên file và số dòng cần đọc
filename = input("Nhập tên file: ")
n = int(input("Nhập số dòng cần đọc: "))

try:
    with open(filename, 'r', encoding='utf-8') as f:
        for i in range(n):
            line = f.readline()
            if not line:
                break
            print(line.strip())
except FileNotFoundError:
    print("Không tìm thấy file!")