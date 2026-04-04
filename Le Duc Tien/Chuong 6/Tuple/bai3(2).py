_tuple = ('ab', 'b', 'e', 'c', 'd', 'e', 'ab')

_new_tuple = ()

for i in _tuple:
    if i not in _new_tuple:
        _new_tuple += (i,)

print(_new_tuple)