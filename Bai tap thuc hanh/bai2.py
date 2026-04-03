filename = input("Nhập tên file để ghi: ")

print("Nhập nội dung (gõ 'END' để kết thúc):")
lines = []
while True:
    line = input()
    if line == "END":
        break
    lines.append(line)

# Ghi vào file
with open(filename, 'w', encoding='utf-8') as f:
    for line in lines:
        f.write(line + '\n')

# Đọc lại và hiển thị
print("\nNội dung file:")
with open(filename, 'r', encoding='utf-8') as f:
    print(f.read())