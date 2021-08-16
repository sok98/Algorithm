# [silver-3] 2606 바이러스
# algorithm BFS
# 메모리: 	 32936 KB
# 시간:      108 ms

import sys
from collections import deque
input = sys.stdin.readline

# 특정 노드가 감염 -> 연결된 모든 노드 감염
# 웜 바이러스에 감염된 컴퓨터 수를 출력

C = int(input()) # 컴퓨터의 수
E = int(input()) # 연결 쌍의 수
graph = [ [0]*(C+1) for _ in range(C+1) ]

for _ in range(E):
    a, b = map(int, input().split()) # 입력받은 연결관계를 그래프에 표현
    graph[a][b] = 1
    graph[b][a] = 1

def bfs(start):
    
    q = deque([start])
    visited = [start]

    while q: # 연결된 노드가 있으면
        current = q.popleft() # queue에서 pop 
        for search in range(len(graph[current])): # 현재 노드와 연결된 노드 중
            if graph[current][search] and search not in visited: # 연결된 간선이 있고 방문한 적 없다면
                visited += [search] # 방문 노드에 추가
                q += [search]  # 연결된 하위 노드를 큐에 추가

    # 모든 연결 노드의 탐색이 끝나면 시작 노드를 제외한 방문 노드의 수를 출력
    return len(visited)-1

print(bfs(1))
