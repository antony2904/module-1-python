#Write a Python program to take a list of integers and 
# remove all duplicate elements while preserving the original order.

def remove_duplicates(numbers: list[int]):
    lst = set()
    unique_numbers = []


    for num in numbers:
        if num not in lst:
            lst.add(num)
            unique_numbers.append(num)

    return unique_numbers

nums = [4, 5, 2, 4, 1, 5, 3, 2, 1, 6]
result = remove_duplicates(nums)

print("Original:", nums)
print("Without duplicates:", result)
