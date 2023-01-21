import sys
sys.setrecursionlimit(10000) # stack stores 10000 functions 

def fibb(n):
    assert n >= 0 and int(n) == n, "variable must be a positive integer"
    if n in [0,1]:
        return n
    else:
        return fibb(n - 1) + fibb(n - 2)

print(fibb(6))

