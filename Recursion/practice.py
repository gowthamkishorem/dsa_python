import sys
sys.setrecursionlimit(10000) # stack stores 10000 functions 

def factorial(n):
    if (n == 0):
        return 1
    else:
        return n * factorial(n-1)

print(factorial(-1))