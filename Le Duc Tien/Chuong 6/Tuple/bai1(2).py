_tuple = ('a', 'b', 'd', 'e')

# chuyển sang list
temp = list(_tuple)

# thêm 'c' vào vị trí index 2
temp.insert(2, 'c')

# chuyển lại thành tuple
_new_tuple = tuple(temp)

print(_new_tuple)