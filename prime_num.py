
#write a python program to find the prime numbers in a given list

lst=[1,4,57,83,7,32,45,98,3,67]

prime_number=[]

for num in lst:
    if num > 1:
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                is_prime = False
                break
        else:
            prime_number.append(num)

print(prime_number)