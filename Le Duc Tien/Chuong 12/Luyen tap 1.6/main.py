# main.py

from math_utils.phanso import cong, tru, nhan, chia
from math_utils.hinhhoc import *
import math_utils
print(dir(math_utils))
# ===== PHÂN SỐ =====
a = (1, 2)  # 1/2
b = (3, 4)  # 3/4

print("Cộng:", cong(a, b))
print("Trừ:", tru(a, b))
print("Nhân:", nhan(a, b))
print("Chia:", chia(a, b))

# ===== HÌNH HỌC =====
r = 5
print("\nChu vi hình tròn:", chu_vi_hinh_tron(r))
print("Diện tích hình tròn:", dien_tich_hinh_tron(r))

dai = 4
rong = 3
print("\nChu vi HCN:", chu_vi_hinh_chu_nhat(dai, rong))
print("Diện tích HCN:", dien_tich_hinh_chu_nhat(dai, rong))