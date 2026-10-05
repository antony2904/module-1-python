from calculator import addition,substraction,multiplication,division

num1 = int(input("Enter your numbers :"))
choice =input("Enter your operation :")
num2 = int(input("Enter your number :"))


if choice == '+':
    print('Result = ',addition(num1,num2))

elif choice == '-':
    print('Result = ',substraction(num1,num2))

elif choice == '/':
    print('Result = ',division(num1,num2))   

else:
    print('Result = ',multiplication(num1,num2))
