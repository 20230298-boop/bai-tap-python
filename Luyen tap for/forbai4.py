n = int(input("Nhập n (<20): "))

if n >= 20:
    print("n phải nhỏ hơn 20")
else:
    print("Các số thỏa mãn:")
    for i in range(1, n+1):
        if i % 5 == 0 or i % 7 == 0:
            print(i, end=" ")