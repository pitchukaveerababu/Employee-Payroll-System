class Employee:
    def __init__(self,emp_id,emp_name,department,salary):
        self.emp_id=emp_id
        self.emp_name=emp_name
        self.department=department
        self.salary=salary
    def display_employee(self):
        print("Employee_id:",self.emp_id)
        print("Employee_name:",self.emp_name)
        print("Department:",self.department)
        print("Salary:",self.salary)
        