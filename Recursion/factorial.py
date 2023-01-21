import sys
sys.setrecursionlimit(10000) # stack stores 10000 functions 

def factorial(n):
    assert n >= 0 and int(n) == n, "variable must be a positive integer"
    if n in [0,1]:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(-1))