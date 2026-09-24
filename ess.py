#Polymorphism – Employee Salary System
#Q1. Write a program to calculate salary for FullTimeEmployee (fixed monthly salary) and 
#PartTimeEmployee (hourly rate × hours worked). Use polymorphism so both classes have a 
#calculate_salary() method.
#Q2. Add a new employee type Freelancer who is paid per project. Show how polymorphism allows handling all 
#employee types in a single loop.

class Employee:

    def __init__(self, name):
        self.name = name

    def calculate_salary(self):
        raise NotImplementedError("Subclasses must implement calculate_salary")


class FullTimeEmployee(Employee):

    def __init__(self, name, monthly_salary):
        super().__init__(name)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary


class PartTimeEmployee(Employee):

    def __init__(self, name, hourly_rate, hours_worked):
        super().__init__(name)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked


class Freelancer(Employee):
    
    def __init__(self, name, pay_per_project, projects_completed):
        super().__init__(name)
        self.pay_per_project = pay_per_project
        self.projects_completed = projects_completed

    def calculate_salary(self):
        return self.pay_per_project * self.projects_completed


employees = [
    FullTimeEmployee("Alice", 6000),
    PartTimeEmployee("John", 25, 80),
    Freelancer("Charlie", 1200, 3),
]

print("- Employee Salaries -")

for employee in employees:
    print(
        f"{employee.name} ({type(employee).__name__}): "
        f"${employee.calculate_salary():,.2f}"
    )