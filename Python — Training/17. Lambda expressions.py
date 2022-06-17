def filtered(iterable, filter):
    return [x for x in iterable if filter(x)]

if __name__ == '__main__':
    print(*filtered(range(101), lambda x: x % 3 == 0), sep=', ')
    print(*filtered(range(101), lambda x: x % 5 == 0), sep=', ')
    print(*filtered(range(101), lambda x: x % 15 == 0), sep=', ')
