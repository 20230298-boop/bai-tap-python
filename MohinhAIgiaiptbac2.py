import tkinter as tk
from tkinter import scrolledtext

# ==========================
# GIẢ LẬP GỌI AI
# ==========================
def goi_mo_hinh_ai(yeu_cau):
    if "phương trình bậc 2" in yeu_cau.lower():
        return '''import tkinter as tk
import math

# Hàm giải phương trình bậc 2
def giai_pt():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())

        if a == 0:
            if b == 0:
                if c == 0:
                    kq.set("Vô số nghiệm")
                else:
                    kq.set("Vô nghiệm")
            else:
                kq.set(f"1 nghiệm: x = {-c/b}")
            return

        delta = b**2 - 4*a*c

        if delta > 0:
            x1 = (-b + math.sqrt(delta)) / (2*a)
            x2 = (-b - math.sqrt(delta)) / (2*a)
            kq.set(f"2 nghiệm: x1 = {x1}, x2 = {x2}")
        elif delta == 0:
            x = -b / (2*a)
            kq.set(f"Nghiệm kép: x = {x}")
        else:
            kq.set("Vô nghiệm")
    except:
        kq.set("Lỗi nhập dữ liệu")

# Giao diện
app = tk.Tk()
app.title("Giải phương trình bậc 2")
app.geometry("400x300")

# Input
label_title = tk.Label(app, text="Giải ax² + bx + c = 0", font=("Arial", 14))
label_title.pack(pady=10)

frame = tk.Frame(app)
frame.pack()

tk.Label(frame, text="a:").grid(row=0, column=0)
entry_a = tk.Entry(frame)
entry_a.grid(row=0, column=1)

tk.Label(frame, text="b:").grid(row=1, column=0)
entry_b = tk.Entry(frame)
entry_b.grid(row=1, column=1)

tk.Label(frame, text="c:").grid(row=2, column=0)
entry_c = tk.Entry(frame)
entry_c.grid(row=2, column=1)

# Button
btn = tk.Button(app, text="Giải", command=giai_pt)
btn.pack(pady=10)

# Kết quả
kq = tk.StringVar()
label_kq = tk.Label(app, textvariable=kq, fg="blue", font=("Arial", 12))
label_kq.pack(pady=10)

app.mainloop()'''
    else:
        return "Chỉ hỗ trợ: giải phương trình bậc 2"


# ==========================
# GIAO DIỆN CHÍNH
# ==========================

def gui_yeu_cau():
    yeu_cau = input_text.get("1.0", tk.END)
    ket_qua = goi_mo_hinh_ai(yeu_cau)

    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, ket_qua)


root = tk.Tk()
root.title("AI Sinh Code")
root.geometry("700x500")

label1 = tk.Label(root, text="Nhập yêu cầu:")
label1.pack()

input_text = scrolledtext.ScrolledText(root, height=5)
input_text.pack(fill=tk.BOTH, padx=10, pady=5)

btn = tk.Button(root, text="Sinh code", command=gui_yeu_cau)
btn.pack(pady=10)

label2 = tk.Label(root, text="Code trả về:")
label2.pack()

output_text = scrolledtext.ScrolledText(root, height=15)
output_text.pack(fill=tk.BOTH, padx=10, pady=5)

root.mainloop()
