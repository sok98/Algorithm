import sys
input = sys.stdin.readline

N = int(input())

tList = []
pList = []
for i in range(N):
    t, p = map(int, input().split())
    tList.append(t)
    pList.append(p)

dp = [0] * 100

for i in range(N):
    if dp[i] > dp[i + 1]:
        dp[i + 1] = dp[i]
    if dp[i + tList[i]] < dp[i] + pList[i]:
        dp[i + tList[i]] = dp[i] + pList[i]

print(dp[N])