def sum_digits(n):
    s = 0
    while n:
        s, n = s + n % 10, n // 10
    return s


num = [i for i in range(1001) if (i % 7 == 0)]

for i in num:
    if(sum_digits(i) % 3 == 0):
        print(i)
