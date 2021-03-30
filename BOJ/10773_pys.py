import sys
c = int(input())
stk = []

for i in range(c):
    n = int(input())
    if n != 0:
        stk.append(n)
    else:
        stk.pop()

for i in stk:
    sum+=i
print(i)
