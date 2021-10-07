# [silver-1] 11660 구간 합 구하기 5
# algorithm  DP
# 메모리:    109344 KB
# 시간:      1324 ms

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
line = [list(map(int, input().split())) for _ in range(N)]
dp = [[0]*(N+1) for _ in range(N+1)]
result = []

for i in range(1, N+1):
  for j in range(1, N+1):
    dp[i][j] = line[i-1][j-1] + dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1]
    
for k in range(M):
  A, B, C, D = map(int, input().split())
  result.append(dp[C][D] - dp[C][B - 1] - dp[A - 1][D] + dp[A - 1][B - 1])

print(*result, sep='\n')
