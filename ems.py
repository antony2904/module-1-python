class Employee:
    company_name = "TechNova Solutions"

    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def emp_details(self):
        print(
            f"Name: {self.name} | Employee ID: {self.employee_id} | "
            f"Salary: ${self.salary} | Company: {self.company_name}"
        )

    @classmethod
    def change_company_name(cls, new_name):
        cls.company_name = new_name


class Developer(Employee):
    def __init__(self, name, employee_id, salary, programming_language):
        super().__init__(name, employee_id, salary)
        self.programming_language = programming_language

    def display_details(self):
        print("--- Developer Details ---")
        super().emp_details()
        print(f"Language: {self.programming_language}\n")


class Manager(Employee):
    def __init__(self, name, employee_id, salary, team_size):
        super().__init__(name, employee_id, salary)
        self.team_size = team_size

    def display_details(self):
        print("--- Manager Details ---")
        super().emp_details()
        print(f"Team Size: {self.team_size} members\n")


dev = Developer("john", "Dev-369", 78000, "Python")
mrg = Manager("alice", "Mrg-789", 89000, 5)

print("Employee Details")
dev.display_details()
mrg.display_details()

Employee.change_company_name("Zyvion Technologies")

print("Updated Employee Details")
dev.display_details()
mrg.display_details()