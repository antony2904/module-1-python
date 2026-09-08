def multiplication_table(number):
    for i in range(1, 11):
        print(f"{number} × {i} = {number * i}")


user = int(input("Enter your number: "))
multiplication_table(user)