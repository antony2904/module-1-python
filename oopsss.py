#encapsulation
#class A:

#    x=10

#    def detail(self):
#        print("hello")
#obj=A()
#print(obj.x)

#obj.detail()


#class A:

#    def __init__(self,name,age):
#        self.name = name
#        self.age = age
    

#    def detail(self):
#        print(f'my name is {self.name} & i am {self.age}')

#obj = A('Antony',23)
#obj.detail()


#class CALCULATOR:

#     def __init__(self,x,y):
#        self.x=x
#        self.y=y

#     def addition(self):
#        sum = self.x+self.y
#        print(f'result = {sum}')

#     def substraction(self):
#         substraction = self.x - self.y
#         print(f'result = {substraction}')

#     def division(self):
#         division = self.x / self.y
#         print(f'result = {division}')

#     def multiplication(self):
#         multiplication = self.x * self.y
#         print(f'result = {multiplication}')

#obj = CALCULATOR(23,56)
#obj.addition()
#obj.substraction()
#obj.division()
#obj.multiplication()

#inheritance
#class Parent:

#    def parent_method(self):
#        print('this is from parent method')

#class Child(Parent):

#    def child_method(self):
#        print('this is from child method')

#    def parent_method(self):
#        print('this is from parent in child method')

#obj=Child()
#obj.child_method()
#obj.parent_method()


#def addition(*args):
#    result=sum(args)
#    print(result)

#def addition(*args):
#    result=sum(args)
#    print(result)


#addition(2,25,75,85,58,66,45)
#addition(5,8,6,2,4,4)


def calculate(a,b):
    result=addition(a,b)
    return result

def addition(a,b):
    return a+b

def substraction(a,b):
    return a-b

def division(a,b):
    return a/b

def multiplication(a,b):
    return a*b


num1 = int(input("Enter first number = "))
num2 = int(input("Enter second number = "))
choice = input("Enter the operator = ")
   
if choice == '+':
    print('Result = ',addition(num1,num2))

elif choice == '-':
    print('Result = ',substraction(num1,num2))

elif choice == '/':
    print('Result = ',division(num1,num2))   

else:
    print('Result = ',multiplication(num1,num2))


#print(calculate(num1,num2))





