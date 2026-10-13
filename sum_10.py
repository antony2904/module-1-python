#Write a Python progran to calculate sum of the first 10 prime numbers 
# without using inbuilt methods ?


def is_prime(n):
    if n < 2:
        return False
    divisor = 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor += 1
    return True

prime_count = 0
total_sum = 0
current_num = 2
primes_found = []

while prime_count < 10:
    if is_prime(current_num):
        primes_found.append(current_num)
        total_sum += current_num
        prime_count += 1
    current_num += 1

print("First 10 prime numbers:", primes_found)
print("Sum of the first 10 prime numbers:", total_sum)