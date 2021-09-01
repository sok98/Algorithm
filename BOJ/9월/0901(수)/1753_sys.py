import heapq
import sys
input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())

INF = int(1e9)
point = [INF]*(V+1)
graph = {n:[] for n in range(1, V+1)}    # 시작 노드 : [(도착 노드, 가중치)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v,w))

def dijkstra(n):
    queue = []
    heapq.heappush(queue, (0, n))
    point[n] = 0

    while queue:
        c, now = heapq.heappop(queue)   # c: 이전 노드까지의 가중치 합 / now: 현재 노드
        # 현재 노드까지의 가중치 합이 이전 노드까지의 가중치 합보다 작을 때 할 필요 없음
        if point[now] < c:  
            continue

        for node in graph[now]:
            cost = c + node[1]

            if cost < point[node[0]]:
                point[node[0]] = cost
                heapq.heappush(queue, (cost, node[0]))

dijkstra(K)
for p in point[1:]:
    if p == INF:
        print("INF")
    else:
        print(p)


