# [gold-5] 14500 테트로미노 (다시풀기)
# algorithm  구현, DFS
# 메모리:     132164 KB
# 시간:       2544 ms - PyPy3

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
result = 0 # 합의 최댓값

d = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 상하좌우
dd = [[(0, -1), (-1, 0), (0, 1)], [(0, -1), (1, 0), (0, 1)], [(-1, 0), (1, 0), (0, 1)], [(-1, 0), (1, 0), (0, -1)]] # ㅗ모양의 각 모서리 

def dfs(r, c, total, visited):
    global result

    if len(visited)==4: # visited는 시작 좌표로부터 타고 들어온 노드의 좌표 리스트
        result = max(result, total)
        return
    for i in range(4): # 상하좌우 탐색
        nr = r + d[i][0]
        nc = c + d[i][1]
        if 0<= nr < N and 0 <= nc < M: # 그래프 범위 내 라면
            if (nr, nc) not in visited:
                visited.append((nr, nc)) # 방문 처리
                dfs(nr, nc, total+graph[nr][nc], visited)
                visited.pop()

def notdfs(r, c):
    global result

    for dir in dd:
        block = graph[r][c] # 중앙 좌표
        for i in range(3):
            nr = r + dir[i][0]
            nc = c + dir[i][1]

            if 0 <= nr < N and 0 <= nc < M: # 범위 내 좌표라면
                block += graph[nr][nc]
            else:
                break
        result = max(result, block)

for r in range(N):
    for c in range(M):
        dfs(r, c, graph[r][c], [(r, c)])
        notdfs(r, c)

print(result)
