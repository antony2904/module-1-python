# x=5
# print(type(x))

# name="John"
# print(type(name))
# print(x == 5)


# x=[1,2,3,4,5,6,7,8]
# x.insert(7,20)


# print(x)


# def detail(x,y):
  #  result=x+y
 #   print(result)

    
#detail(15,345)

#def addition(x,y):
  #  sum = x+y
   # print(f'result = {sum}')
    
#addition(34,56)

#def addition(name,completed,age):
 #   print(f'my name is  {name}\ni have completed my  {completed}\ni am {age}')
    
#addition('antony','engineering','23')

#x = 16

#if x == 18:
 #   print("true")

#else :
 #   print("false")
 
#lst=[15,16,17,18,19]

#for i in lst:
 #   print(i)
    
#for i in range(0,250,25):
 #   print(i)
 
 
#lst = [45,87,96,57,37,86,92]

#new_lst=[]

#for i in lst:
 #   if i>75:
  #      new_lst.append(i)
#print(new_lst)
    
# list comprehension ( expression for i in iterable)

#lst = [45,87,96,57,37,86,92]

#new_lst=[]

#for i in lst:
  #  result =i* 3
 #   new_lst.append(result)

#print(new_lst)

#lst=[0,1,2,3,4,5,6,7,8,9,10]
<<<<<<< HEAD

#new_lst=[]
#for i in lst:
#    if i % 2 == 0:
#        new_lst.append(i)

#print(new_lst)

#def fibonacci_sum(n):
#    if n <= 0:
#        return 0
    
#    fib_list = [0, 1][:n] 
    
#    while len(fib_list) < n:
#       next_fib = fib_list[-1] + fib_list[-2]
#        fib_list.append(next_fib)
        
#    print(f"First {n} Fibonacci numbers: {fib_list}")
#    print(f"Sum: {sum(fib_list)}")

#fibonacci_sum(5) 

#name = "Alex"
#age = 25
#city = "Kochi"

#print(f"My name is {name}, I am {age} years old, and I live in {city}.")

#a = 5
#b = 10

#a, b = b, a

#print("a:", a, "b:", b) 

#length = 100
#width = 25
#area = length * width

#print(f"The area of the rectangle is {area}")

#string_num = "50"
#result = int(string_num) + 100

#print(result) 

#my_tuple = (1,2,3)
#my_tuple[0] = 10

#list1 = [1, 2, 3, 4]
#list2 = [4, 5, 6, 7]

#if set(list1) & set(list2):
#    print("The lists have at least one common element.")
#else:
#    print("No common elements.")

#def is_prime(n):
#    if n <= 1:
#        return False
#    for i in range(2, int(n**0.5) + 1):
#        if n % i == 0:
#            return False
#    return True

#print(is_prime(11)) 

#def is_palindrome(word):
#    word = word.lower()
#    return word == word[::-1]

#print(is_palindrome("Racecar")) 

#def add(x, y): return x + y
#def subtract(x, y): return x - y
#def multiply(x, y): return x * y
#def divide(x, y): return x / y if y != 0 else "Cannot divide by zero"

#print("Add: ", add(10, 5))
#print("Divide: ", divide(10, 0))

#def check_even_odd(num):
#    if num % 2 == 0:
#        print(f"{num} is Even")
#    else:
#        print(f"{num} is Odd")

#check_even_odd(257)

#def reverse_number(n):
#    return int(str(n)[::-1])

#print(reverse_number(12345)) 

#def divide_numbers(a, b):
#    try:
#        result = a / b
#    except ZeroDivisionError:
#        print("Error: You cannot divide by zero!")
#    else:
#        print(f"Success! The result is {result}")
#    finally:
#       print("Execution of divide_numbers completed.\n")

#divide_numbers(10, 2)
#divide_numbers(10, 0)




    


    
=======

#new_lst=[]
#for i in lst:
  #  if i % 2 == 0:
 #       new_lst.append(i)

#print(new_lst)

#def fibonacci_sum(n):
#    if n <= 0:
#        return 0
    
#    fib_list = [0, 1][:n] 
    
#    while len(fib_list) < n:
#       next_fib = fib_list[-1] + fib_list[-2]
#        fib_list.append(next_fib)
        
#    print(f"First {n} Fibonacci numbers: {fib_list}")
#    print(f"Sum: {sum(fib_list)}")

#fibonacci_sum(5) 

#name = "Alex"
#age = 25
#city = "Kochi"

#print(f"My name is {name}, I am {age} years old, and I live in {city}.")

#a = 5
#b = 10

#a, b = b, a

#print("a:", a, "b:", b) 

#length = 100
#width = 25
#area = length * width

#print(f"The area of the rectangle is {area}")

#string_num = "50"
#result = int(string_num) + 100

#print(result) 

#my_tuple = (1,2,3)
#my_tuple[0] = 10

#list1 = [1, 2, 3, 4]
#list2 = [4, 5, 6, 7]

#if set(list1) & set(list2):
#    print("The lists have at least one common element.")
#else:
#    print("No common elements.")

#def is_prime(n):
#    if n <= 1:
#        return False
#    for i in range(2, int(n**0.5) + 1):
#        if n % i == 0:
#            return False
#    return True

#print(is_prime(11)) 

#def is_palindrome(word):
#    word = word.lower()
#    return word == word[::-1]

#print(is_palindrome("Racecar")) 

#def add(x, y): return x + y
#def subtract(x, y): return x - y
#def multiply(x, y): return x * y
#def divide(x, y): return x / y if y != 0 else "Cannot divide by zero"

#print("Add: ", add(10, 5))
#print("Divide: ", divide(10, 0))

#def check_even_odd(num):
#    if num % 2 == 0:
#        print(f"{num} is Even")
#    else:
#        print(f"{num} is Odd")

#check_even_odd(257)

#def reverse_number(n):
#    return int(str(n)[::-1])

#print(reverse_number(12345)) 

#def divide_numbers(a, b):
#    try:
#        result = a / b
#    except ZeroDivisionError:
#        print("Error: You cannot divide by zero!")
#    else:
#        print(f"Success! The result is {result}")
#    finally:
#       print("Execution of divide_numbers completed.\n")

#divide_numbers(10, 2)
#divide_numbers(10, 0)

>>>>>>> 25c3e3964b2b94504344eefa47f976260f21a45c



