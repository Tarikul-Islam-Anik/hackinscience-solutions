import itertools


def is_prime(n):
    return n > 1 and all(n % num != 0 for num in range(2, int(n ** 0.5) + 1))


for i in itertools.count(start=100000000, step=1):
    if is_prime(i) and i > 100000000:
        print(i)
        break
