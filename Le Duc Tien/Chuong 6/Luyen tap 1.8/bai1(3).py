code_dict = {'a': '!', 'b': '@', 'c': '#', 'd': '$'}
def encode(text, code_dict):
    result = ""
    for char in text:
        if char in code_dict:
            result += code_dict[char]
        else:
            result += char  # giữ nguyên nếu không có trong bảng mã
    return result
def decode(text, code_dict):
    # đảo ngược dictionary
    reverse_dict = {v: k for k, v in code_dict.items()}
    
    result = ""
    for char in text:
        if char in reverse_dict:
            result += reverse_dict[char]
        else:
            result += char
    return result
code_dict = {'a': '!', 'b': '@', 'c': '#', 'd': '$'}

text = "abcd xyz"

encoded = encode(text, code_dict)
print("Mã hóa:", encoded)

decoded = decode(encoded, code_dict)
print("Giải mã:", decoded)