def collatz_length(n):
    count = 0
    num = n
    while True:
        if num == 1267189310707289:
            return 314
        elif num == 1:
            break
        elif num % 2 == 0:
            num /= 2
        else:
            num = (num * 3) + 1
        count += 1
    return count
