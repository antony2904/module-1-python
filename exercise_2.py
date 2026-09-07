#1.Write a Python program to take a list of integers and 
#remove all duplicate elements while preserving the original order.

lst= [5, 2, 9, 2, 5, 3, 7, 9]


new_lst=[]
for i in lst:
    if i not in new_lst:
        new_lst.append(i)

print( new_lst)

#2.Write a Python program that checks whether a given string is a palindrome  or not.


def is_palindrome(text):
    return text == text[::-1]

word = "web"
if is_palindrome(word):
    print(f"'{word}' is a palindrome!")
else:
    print(f"'{word}' is not a palindrome.")

#3.Write a Python program to generate the first N terms of the Fibonacci series using iteration.
#Input: N = 10    


def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return[0]
    
    fib_series = [0, 1]

    for _ in range(2, n):

        next_term = fib_series[-1] + fib_series[-2]
        fib_series.append(next_term)

    return fib_series

N = 10

result = fibonacci(N)
print(f"The first {N} terms of the Fibonacci series are:")
print(result)    



#4.Write a Python progran to calculate sum of the first 10
#  prime numbers without using inbuilt methods ?


prime_number = 0
input_number = 2
sum = 0

while prime_number < 10:
    prime = True
    
    for i in range(2, input_number):
        if input_number % i == 0:
            prime = False  
            break             
            
    if prime == True:
        sum = sum + input_number
        prime_number = prime_number + 1
        
    input_number = input_number + 1

print("The sum of the first 10 prime numbers is:", sum)


#5.Write a python program to flatten a 2D list using list comprehension ?


def flatten_2d_list_traditional(matrix):
    flat_list = []
    
    for sublist in matrix:
        for item in sublist:
            flat_list.append(item)
            
    return flat_list

two_d_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
flattened_result = flatten_2d_list_traditional(two_d_list)

print(f"Original 2D list: {two_d_list}")
print(f"Flattened list:   {flattened_result}")

#6.Write a python program to replace prime numbers in a list with the factorial of the number ?

lst = [4, 5, 8, 3, 10, 7]
new_lst = []

for num in lst:
    
    prime = True
    
    if num <= 1:
        prime = False
    else:
        for i in range(2, num):
            if num % i == 0:
                prime = False
                break
                
    if prime == True:
        factorial = 1
        for j in range(1, num + 1):
            factorial = factorial* j
            
        new_lst.append(factorial)
        
    else:
        new_lst.append(num)

print("lst:", lst)
print("new_lst:", new_lst)
