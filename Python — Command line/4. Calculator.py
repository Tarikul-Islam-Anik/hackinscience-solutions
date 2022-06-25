import sys

try:
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    c = sys.argv[2]

    if c == "+":
        print(a + b)
    elif c == "-":
        print(a - b)
    elif c == "*":
        print(a * b)
    elif c == "/":
        print(a / b)
    elif c == "%":
        print(a % b)
    elif c == "^":
        print(a**b)
    else:
        print("input error")
except IndexError:
    print("usage: ./solution.py a_number (an_operator +-*/%^) a_number")
    sys.exit(1)
except ZeroDivisionError:
    print("input error")
    sys.exit(1)
except ValueError:
    print("input error")
    sys.exit(1)
