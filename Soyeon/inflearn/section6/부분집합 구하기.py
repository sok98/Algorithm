# [section-6] 부분집합 구하기

import sys
input = sys.stdin.readline

N = int(input())
result = []

def dfs(v):
  if v==N+1:
      for i in range(1, N+1):
        if ch[i] == 1:
          print(i, end=' ')
      print()
  else:
    ch[v]=1
    dfs(v+1)
    ch[v]=0
    dfs(v+1)

ch = [0]*(N+1)
dfs(1)
print(''.join(result))
