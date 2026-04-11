from .employee import Employee

class Manager(Employee):
    def __init__(self, emp_id, name, age, coefficient):
        super().__init__(emp_id, name, age, coefficient)