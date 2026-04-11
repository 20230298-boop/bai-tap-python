class Employee:
    BASE_SALARY = 1000

    def __init__(self, emp_id, name, age, coefficient):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.coefficient = coefficient
        self.performance = 0
        self.projects = []

    def get_salary(self):
        return self.coefficient * self.BASE_SALARY

    def __str__(self):
        return (f"{self.emp_id} - {self.name} - {self.age} tuổi "
                f"- Hệ số: {self.coefficient} - Lương: {self.get_salary()} "
                f"- Projects: {len(self.projects)}")