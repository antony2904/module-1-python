#1. What is the output of the following code? Explain why the result occurs.
#x = [1, 2, 3]  #lst
#y = x  
#z = x.copy() #creating a new lst with same values,but it is a separate obj
#y.append(4) #changes the orginal lst
#z.append(5) 
#print(x, y, z)

#output
# x = [1,2,3,4]
# y = [1,2,3,4]
# z = [1,2,3,5]




#2. Predict the output without executing the program. 
#   Pay particular attention to Python's late binding behavior.


#funcs = [] 
#for i in range(5): 
#    funcs.append(lambda: i) 
#print([f() for f in funcs])

#output = [4, 4, 4, 4, 4]

#   How would you modify the code so that it prints [0, 1, 2, 3, 4]?

#funcs = []
#for i in range(5):
#    funcs.append(lambda i=i: i)

#print([f() for f in funcs])



#3. What will be printed? Explain the role of mutable default arguments.

#def add_item(item, items=[]): 
#    items.append(item) 
#    return items 

#print(add_item(1)) #uses the default lst and make it ,output [1]
#print(add_item(2)) #uses the same default lst again ,output [1,2]
#print(add_item(3,[])) #passes a new empty lst ,output [3] (mutable defult argument)
#print(add_item(4)) # uses the orginal default lst again , output [1,2,4]


#if we didn,t add new empty lst the output will be 
#def add_item(item, items=[]): 
#    items.append(item) 
#    return items 

#print(add_item(1)) 
#print(add_item(2)) 
#print(add_item(3)) 
#print(add_item(4))

#output
#[1]
#[1, 2]
#[1, 2, 3]
#[1, 2, 3, 4]


#4. Determine the output and explain the evaluation order.
#Then explain how Python performs the assignment internally.

#a = 10 
#b = 20 
#a, b = b, a + b # values are swapped here  10 , 20 = 20 , 10 + 20
#print(a, b)                                #         20,30 
                                           #         a , b    


#5. What is the output? Explain the difference between is and == in this example.

#a = 256 
#b = 256 
#c = 257 
#d = 257 
#print(a is b) #check whether two variables point to the same object in lst
#print(c is d) #check whether two variables point to the same object in lst
#print(a == b, c == d) #check whether the values are equal.



#10. What is the output of this code? Explain the behavior of yield and function state
#def f(): 
#    print("A") 
#    yield 1 
#    print("B") 
#    yield 2 

#g = f() # f() returns a generator, so its body does not run until next(g) is called.

#print(next(g)) # The first next() runs until yield 1 and pauses. The second next() resumes

#print(next(g)) # from that point, prints B, yields 2, and pauses again.


# Output:
# A
# 1
# B
# 2

#14.what is the output?
#Explain attribute lookup and class-level attributes.

#class A: 
#    x = 10 
#class B(A): 
#    x = 20 

#a = A()
#b = B()
#print(a.x, b.x) # a.x is found on A. b.x is found on B
#A.x = 30 # overrides A.x. After A.x is changed
#print(a.x, b.x) #a sees the new class attribute, while b still uses B.x = 20.


# Output:
# 10 20
# 30 20


#19. What is printed, and why? 

#def outer(): 
#    x = 10 
#    def inner(): 
#        nonlocal x # nonlocal allows inner to update that same x instead of creating a local one.
#        x += 5
#        return x 
#    return inner 
#f = outer() # outer() returns inner, and inner keeps the enclosing x alive in a closure.
#print(f()) 
#print(f())

# Output:
# 15
# 20

#21. Explain the output and exception behavior. 
#Then explain what changes if the except block itself raises an exception.


#try: 
#    print(10 / 0) # 10 / 0 raises ZeroDivisionError, so the except block runs and the else block
                  # is skipped. The finally block runs whether or not an exception occurs.

#except ZeroDivisionError: # If the except block raises another exception, finally still runs first, and
                          # the new exception then propagates unless another handler catches it.
#     print("zero") 
#else: 
#    print("else") 
#finally: print("finally") 

# Output:
# zero
# finally


#17. Write a function that accepts a list of strings and groups anagrams together. 
# Example: ["eat", "tea", "tan", "ate", "nat", "bat"] 
# Expected groups may be: [["eat","tea","ate"], ["tan","nat"], ["bat"]]. 
# Target O(n·k log k) or better, where n is the number of words and k is average word length.

lst =["eat", "tea", "tan", "ate", "nat", "bat"] 


def group_anagrams(words): # Anagrams have the same sorted-letter key. Sorting each word costs O(k log k),
    groups = {}
    for word in words:  # so processing n words costs O(n * k log k) overall.
        key = tuple(sorted(word))
        groups.setdefault(key, []).append(word)
    return list(groups.values())


words = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(words))

# Output:
# [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]



