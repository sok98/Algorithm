import sys
n = int(sys.stdin.readline())
arr=[]

for i in range(n):
    arr.append(int(sys.stdin.readline()))

table = [[0 for _ in range(3)] for _ in range(n)]
for i in range(n):
    for j in range(3):
        if i == 0:
            table[i][j] = arr[i][j]
        else:
            table[i][j] = min(table[i-1][(j+1)%3], table[i-1][(j+2)%3]) + arr[i][j]
print(min(table[-1]))