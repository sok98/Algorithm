import sys 
import math
n,r = map(int, sys.stdin.readline().split())

def factorial(num):
    result = 1 
    for i in range(1,num + 1): 
        result *= i 
    return result 

print(int(factorial(n) / (factorial(n - r) * factorial(r))))

