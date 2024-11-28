def powers_of_three():
    n = 0
    while True:
        yield 3 ** n
        n += 1

gen = powers_of_three()
for _ in range(10):
    print(next(gen))
