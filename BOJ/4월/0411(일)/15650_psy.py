import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().split(" "))
li = []
for i in range(1,n+1):
    li.append(i)

for each in list(combinations(li, m)):
    for num in each:
        print(num, end=" ")
    print()