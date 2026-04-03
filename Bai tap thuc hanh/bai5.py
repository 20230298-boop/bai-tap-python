# Đọc file
with open("demo_file2.txt", "r", encoding="utf-8") as f:
    content = f.read()

# Chuẩn hóa dữ liệu
content = content.lower()  # chuyển về chữ thường
words = content.split()    # tách từ

# Đếm số lần xuất hiện
result = {}
for word in words:
    if word in result:
        result[word] += 1
    else:
        result[word] = 1

# In kết quả
print(result)