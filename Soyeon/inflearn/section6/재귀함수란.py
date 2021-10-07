# [section-6] 재귀함수란

import sys
input = sys.stdin.readline

N = int(input())
result = []

def dfs(x):
  if x>0:
    dfs(x//2)
    result.append(str(x%2))

dfs(N)
print(''.join(result))
