#Write a Python program to generate the first N terms of the 
# Fibonacci series using iteration.

#Input: N = 10
#Output: 0 1 1 2 3 5 8 13 21 34

N = 10

a, b = 0, 1

for _ in range(N):
  print(a, end=" ")
  a, b = b, a + b