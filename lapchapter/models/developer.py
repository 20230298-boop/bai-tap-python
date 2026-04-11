from .employee import Employee

class Developer(Employee):
    def __init__(self, emp_id, name, age, coefficient, language):
        super().__init__(emp_id, name, age, coefficient)
        self.language = language