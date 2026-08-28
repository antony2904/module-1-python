class employee:
    company_name = "tech_lead."

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def details(self):
        print(f"Name: {self.name }  | Salary: $  {str(self.salary) } | Company: {self.company_name }")

    def change_company(cls, new_company):
        cls.company_name = new_company

    change_company = classmethod(change_company)

    def valid_salary(salary):
        return salary > 0

    valid_salary = staticmethod(valid_salary)



emp1 = employee("Alice Smith", 55000)
emp2 = employee("Bob Jones", 62000)
emp3 = employee("Charlie Brown", 45000)

print("--- Initial Employee Details ---")
emp1.details()
emp2.details()
emp3.details()
print()

test_salary_1 = 70000
test_salary_2 = -5000

print("--- Salary Validation ---")
print(
    "Is $"
    + str(test_salary_1)
    + " valid? "
    + str(employee.valid_salary(test_salary_1))
)
print(
    "Is $"
    + str(test_salary_2)
    + " valid? "
    + str(employee.valid_salary(test_salary_2))
)
print()

print("--- Updating Company Name ---")
employee.change_company("Innovate Solutions")

emp1.details()
emp2.details()
emp3.details()