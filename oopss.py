#class Details :

#    def client_details (self,name):

#        print(f'client name : {name}')


#obj = Details ()
#obj.client_details('John')


#calculator

#class Calculator :

#    def addition(self,x,y):
#        return x+y

#    def substraction(self,x,y):
#        return x-y

#    def division(self,x,y):
#        try:
#            return (x/y)
#        except ZeroDivisionError:
#            print("Error:you cannot divide by zero!")
#        finally:
#            print("execution of divide number is completed.")

#    def multiplication(self,x,y):
#        return x*y


#num1 = int(input("Enter first number = "))
#num2 = int(input("Enter second number = "))
#choice = input("Enter the operator = ")

#obj = Calculator()

#if choice == '+':
#    print('Result = ',obj.addition(num1,num2))

#elif choice == '-':
#    print('Result = ',obj.substraction(num1,num2))

#elif choice == '/':
#    print('Result = ',obj.division(num1,num2))   

#else:
#    print('Result = ',obj.multiplication(num1,num2))

#print(obj.addition(num1,num2))
#print(obj.substraction(num1,num2))
#print(obj.division(num1,num2))
#print(obj.multiplication(num1,num2))



#inheritance

#class Parent:

#    x = 5
#    def parent_method(self):
#        print('this is from parent method')

#class Child:

#    x = 20
#    def child_method(self):
#        print('this is a child method')

#    def parent_method(self):
#        print('this is from child method')



#obj = Parent()
#obj1 = Child()
#obj.parent_method()
#print(obj.x)
#obj1.child_method()
#obj1.parent_method()
#print(obj1.x)

#def detail(**kwargs):
#    print (f"my  name is {kwargs['name']}, i am {kwargs['age']} year old, i am working in {kwargs['department']} section")


#detail(name='John',age=28,department='accounts')



class Student_detail:

  def __init__(self, name, age, department):
    self.name = name
    self.age = age
    self.department = department


  def student_detail(self, ):
    print(f"Student name:{self.name}, Student age:{self.age},Department:{self.department}")


  

obj = Student_detail('Rahul', 22, 'CS')
obj.student_detail()


