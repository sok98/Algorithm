import sys
from collections import defaultdict

n = int(sys.stdin.readline())
count = defaultdict(lambda : 0)

def calcul(num, n):
    if count[num] == 0 or count[num] > count[n] + 1:
        count[num] = count[n] + 1

        if num%3 == 0:
            calcul(num//3, num)
        if num%2 == 0:
            calcul(num//2, num)
        elif num > 1:
            calcul(num-1, num)
        

if n%3 == 0:
    calcul(n//3, n)
if n%2 == 0:
    calcul(n//2, n)
elif n > 1:
    calcul(n-1, n)

print(count[1])