import sys
input = sys.stdin.readline

T = int(input())
point = [list(map(int, input().split())) for _ in range(T)]

for i in range(T):
    n = ((point[i][3] - point[i][0]) ** 2 +
         (point[i][4] - point[i][1]) ** 2) ** 0.5
    k1 = point[i][2]
    k2 = point[i][5]

    if n == 0:
        if k1 == k2:
            print(-1)
        else:
            print(0)
    elif n == k1 + k2 or n == abs(k1 - k2):
        print(1)
    elif n > k1 + k2:
        print(0)
    elif n < k1 + k2:
        if n < max(k1, k2):
            print(0)
        else:
            print(2)
