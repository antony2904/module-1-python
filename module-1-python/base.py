#Create a base class Person with attributes name and age. 
# Derive a class Employee that adds salary. 
# Show how to create an object of Employee and display all details.
class Person:

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def display_person_details(self):
        print(f"Name:{self.name}")
        print(f"Age:{self.age}")


class Employee(Person):

    def __init__(self, name: str, age: int, salary: float):
        super().__init__(name, age)
        self.salary = salary

    def display_details(self):
        self.display_person_details()
        print(f"Salary: ${self.salary:,.2f}")

if __name__ == "__main__":
    emp = Employee(name="john xavier", age=32, salary=85000)
    emp.display_details()