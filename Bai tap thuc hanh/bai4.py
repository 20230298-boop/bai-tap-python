# Nhập thông tin
ten = input("Nhập tên: ")
tuoi = input("Nhập tuổi: ")
email = input("Nhập email: ")
skype = input("Nhập skype: ")
dia_chi = input("Nhập địa chỉ: ")
noi_lam_viec = input("Nhập nơi làm việc: ")

# Lưu vào file
with open("setInfo.txt", "w", encoding="utf-8") as f:
    f.write(f"Tên: {ten}\n")
    f.write(f"Tuổi: {tuoi}\n")
    f.write(f"Email: {email}\n")
    f.write(f"Skype: {skype}\n")
    f.write(f"Địa chỉ: {dia_chi}\n")
    f.write(f"Nơi làm việc: {noi_lam_viec}\n")

print("\nĐã lưu vào file setInfo.txt")

# Đọc file và hiển thị
print("\n--- Nội dung file ---")
with open("setInfo.txt", "r", encoding="utf-8") as f:
    print(f.read())