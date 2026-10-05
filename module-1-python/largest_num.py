#Write a python program to find the largest number in a list 

lst = [456,78,345,232.377,234,1000,5673,15434]

largest = lst[0]
secondlargest =lst[0]

for i in range(len(lst)):
    j = i+1
    for j in range(len(lst)):
        if lst[j]> largest:
            largest = lst[j]

for i in range(len(lst)):
    j = i+1
    for j in range(len(lst)):
        if lst[j] > secondlargest and lst[j] <largest:
            secondlargest = lst[j]


print(largest)
print(secondlargest)