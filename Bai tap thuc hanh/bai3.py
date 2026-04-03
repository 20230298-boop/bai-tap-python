filename = "demo_file1.txt"

# Tạo file và ghi nội dung
with open(filename, 'w', encoding='utf-8') as f:
    f.write("Thực hành\n")
    f.write("n voi n file\n")
    f.write("n IO\n")

# a) In nội dung trên một dòng
print("a) Nội dung trên 1 dòng:")
with open(filename, 'r', encoding='utf-8') as f:
    content = f.read().replace('\n', ' ')
    print(content)

# b) In theo từng dòng
print("\nb) Nội dung theo từng dòng:")
with open(filename, 'r', encoding='utf-8') as f:
    for line in f:
        print(line.strip())