from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
numbers = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    row = map(int, input().split())
    numbers[i][1:] =row

gaps = [tuple(map(int, input().split())) for _ in range(M)]
S = [[0] * (N + 1) for _ in range(N + 1)]
answer = []

for i in range(1, N + 1):
    for j in range(1, N + 1):
        S[i][j] = S[i-1][j] + S[i][j - 1] - S[i - 1][j - 1] + numbers[i][j]

for x1, y1, x2, y2 in gaps:
    if x1 == 0 and y1 == 0:
        print(S[x2][y2])
    elif x1 == 0:
        print(S[x2][y2] - S[x2][y1 - 1])
    elif y1 == 0:
        print(S[x2][y2] - S[x1 - 1][y2])
    else:
        print(S[x2][y2] - S[x2][y1 - 1] - S[x1 - 1][y2] + S[x1 - 1][y1 - 1])
