_tuple = ('ab', 'b', 'e', 'c', 'd', 'e', 'ab')

_new_tuple = ()

for i in _tuple:
    if _tuple.count(i) == 1:
        _new_tuple += (i,)

print(_new_tuple)