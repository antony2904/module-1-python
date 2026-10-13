def generator_fun():
    yield 10
    yield 20
    yield 30

x = generator_fun()

print(next(x))
print(next(x))
