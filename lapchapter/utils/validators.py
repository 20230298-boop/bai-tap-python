from exceptions.employee_exceptions import *

def validate_age(age):
    if age < 18 or age > 65:
        raise InvalidAgeError("Tuổi phải từ 18-65")

def validate_score(score):
    if score < 0 or score > 10:
        raise ValueError("Điểm phải từ 0-10")

def validate_coefficient(c):
    if c <= 0:
        raise ValueError("Hệ số phải > 0")