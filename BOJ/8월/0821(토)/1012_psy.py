# [silver-2] 1012 유기농 배추
# algorithm  DFS/BFS, 그래프 이론
# 메모리:    31544 KB
# 시간:      408  ms

import sys
sys.setrecursionlimit(10000)

def dfs(r,c):
    dd = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 상하좌우

    a[r][c] = -1  # 방문체크
    for d in range(4):
        nr = r + dd[d][0]
        nc = c + dd[d][1]
        if nr < 0 or nr >= N or nc < 0 or nc >= M:  # 범위체크
            continue
        if a[nr][nc] == 1:
            a[nr][nc] = -1  # 방문체크
            dfs(nr,nc)

T = int(input())
result = []
for tc in range(1, T+1):
    M, N, K = map(int, input().split())
    a = [[0] * M for _ in range(N)] 

    for _ in range(K): 
        c, r = map(int, input().split())
        a[r][c] = 1

    count = 0
    for i in range(N):
        for j in range(M):
            if a[i][j] == 1:
                dfs(i,j)
                count += 1
    result.append(count)

for r in result:
    print(r)
