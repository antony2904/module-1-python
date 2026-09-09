def addition(x,y):
    return  (x+y)

def substraction(x,y):
    return  (x-y)

def multiplication(x,y):
    return (x*y)

def division(x,y):
    try:
        return (x/y)
    except ZeroDivisionError:
        print("Error:you cannot divide by zero!")
    finally:
        print("execution of divide number is completed.")


  

