# phanso.py

def cong(a, b):
    tu = a[0]*b[1] + b[0]*a[1]
    mau = a[1]*b[1]
    return (tu, mau)

def tru(a, b):
    tu = a[0]*b[1] - b[0]*a[1]
    mau = a[1]*b[1]
    return (tu, mau)

def nhan(a, b):
    return (a[0]*b[0], a[1]*b[1])

def chia(a, b):
    return (a[0]*b[1], a[1]*b[0])