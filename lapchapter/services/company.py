from exceptions.employee_exceptions import *

class Company:
    def __init__(self):
        self.employees = []
        self.projects = {}

    # ===== EMPLOYEE =====
    def add_employee(self, emp):
        for e in self.employees:
            if e.emp_id == emp.emp_id:
                raise DuplicateEmployeeError()
        self.employees.append(emp)

    def find_by_id(self, emp_id):
        for e in self.employees:
            if e.emp_id == emp_id:
                return e
        raise EmployeeNotFoundError(emp_id)

    def list_all(self):
        if not self.employees:
            raise IndexError("Chưa có dữ liệu")
        for e in self.employees:
            print(e)

    def total_salary(self):
        return sum(e.get_salary() for e in self.employees)

    def top_3_salary(self):
        return sorted(self.employees, key=lambda x: x.get_salary(), reverse=True)[:3]

    # ===== PROJECT =====
    def assign_project(self, emp_id, project_name):
        emp = self.find_by_id(emp_id)

        if project_name not in self.projects:
            self.projects[project_name] = []

        if emp not in self.projects[project_name]:
            self.projects[project_name].append(emp)
            emp.projects.append(project_name)

    def get_project_members(self, project_name):
        if project_name not in self.projects:
            raise ProjectAllocationError("Dự án không tồn tại")
        return self.projects[project_name]

    def top_10_most_projects(self):
        return sorted(self.employees, key=lambda e: len(e.projects), reverse=True)[:10]

    def top_10_least_projects(self):
        return sorted(self.employees, key=lambda e: len(e.projects))[:10]

    # ===== HR =====
    def remove_multiple_employees(self, ids):
        removed = []
        for emp_id in ids:
            try:
                emp = self.find_by_id(emp_id.strip())
                self.employees.remove(emp)
                removed.append(emp_id)
            except:
                pass
        return removed