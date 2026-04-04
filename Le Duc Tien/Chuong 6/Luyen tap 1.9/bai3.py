_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

even = []  # số chẵn
odd = []   # số lẻ

for i in _list:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print("Số chẵn:", even)
print("Số lẻ:", odd)