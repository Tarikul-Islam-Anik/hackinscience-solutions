import sys

try:
    print(int(sys.argv[1]) + int(sys.argv[2]))
except:
    print("usage: python3 solution.py OP1 OP2")
