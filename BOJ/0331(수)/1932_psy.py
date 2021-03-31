import sys
n = int(sys.stdin.readline())
num = []

for i in range(n):
    num.append(list(map(int, sys.stdin.readline().split())))

for i in range(1,n):
    for j in range(len(num[i])):
        if j==0: # 맨왼쪽
            num[i][j] += num[i-1][j]
        elif j==i: # 맨오른쪽
            num[i][j] += num[i-1][j-1]
        else: # 가운데
            num[i][j] += max(num[i-1][j], num[i-1][j-1])

print(max(num[n-1]))