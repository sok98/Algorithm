# [silver-2] 11724 연결 요소의 개수
# algorithm  DFS/BFS, 그래프 이론
# 메모리:    36252 KB
# 시간:      744 ms

import sys
input = sys.stdin.readline

N,M=map(int,input().split())
graph=[[0]*(N+1)for i in range(N+1)]

for i in range(M):
    a, b=map(int,input().split())
    graph[a][b]=graph[b][a]=1

visited=[0]*(N+1)
count=0

def bfs(v):
    queue=[v]
    while queue:
        v=queue.pop(0)
        for i in range(1,N+1):
            if graph[i][v]==1 and visited[i]==0:
                visited[i]=1
                queue.append(i)

for i in range(1,N+1):
    if visited[i]==0:
        bfs(i)
        count+=1

print(count)