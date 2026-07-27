def add(*args):
    total = 0
    for n in args:
        total = n + total
    return total


print(add(1, 4, 6, 8))
