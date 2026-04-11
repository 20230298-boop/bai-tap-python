from .employee import Employee

class Intern(Employee):
    def __init__(self, emp_id, name, age, coefficient):
        super().__init__(emp_id, name, age, coefficient)