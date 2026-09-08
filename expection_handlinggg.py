def divide_number(x,y):
  try:
    result = x/y
  except ZeroDivisionError:
    print("Error:you cannot divide by zero!")
  #else:
  #  print(f"sucess,the result is {result}")
  finally:
    print("execution of divide number is completed.")

divide_number(10,2)
divide_number(10,0)