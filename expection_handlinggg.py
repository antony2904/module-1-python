number = int(input("Enter the number : \n"))
try:
    result = 10/number
    print(result)
except ZeroDivisionError :
    print("Error:you cannot divide by zero!")
 
finally:
    print("execution of divide number is completed.")
