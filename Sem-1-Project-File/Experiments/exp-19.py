class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id
    def get_details(self):
        return f"Employee: {self.name}, ID: {self.employee_id}"

class Manager(Employee):
    def __init__(self, name, employee_id, team_size):
        super().__init__(name, employee_id)
        self.team_size = team_size
    def get_details(self):
        return f"Manager: {self.name}, ID: {self.employee_id}, Team Size: {self.team_size}"
    
class Developer(Employee):
    def __init__(self, name, employee_id, programming_language):
        super().__init__(name, employee_id)
        self.programming_language = programming_language
    def get_details(self):
        return f"Developer: {self.name}, ID: {self.employee_id}, Language: {self.programming_language}"
    
def print_employee_details(employees):
    for employee in employees:
        print(employee.get_details())
employees = [Manager("Rohan", 118, 10),Developer("Aditya", 115, "Python"),Employee("Dev", 125)]
print_employee_details(employees)