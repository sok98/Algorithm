# [gold-4] 19238 스타트와 택시
# algorithm 그래프, 구현, DFS/BFS
# 메모리:   31916 KB
# 시간:     708 ms

import sys
from collections import deque
input = sys.stdin.readline

N, M, fuel = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
X, Y = map(int, input().split())  # 시작 좌표
people = [list(map(int, input().split())) for _ in range(M)]  # 출발지 행, 열, 목적지 행, 열

direction = [(-1, 0), (0, -1), (1, 0), (0, 1)]


def bfs(X, Y):
    visited = [[-1] * N for _ in range(N)]
    queue = deque()
    queue.append((X, Y))
    visited[X][Y] = 0

    while queue:
        pop_x, pop_y = queue.popleft()

        for i in range(4):  # 상하좌우 벽이 아닌 지점 탐색
            n_x, n_y = pop_x + direction[i][0], pop_y + direction[i][1]

            if n_x < 0 or n_x >= N or n_y < 0 or n_y >= N:
                continue
            if board[n_x][n_y] == 1 or visited[n_x][n_y] != -1:
                continue

            visited[n_x][n_y] = visited[pop_x][pop_y] + 1
            queue.append((n_x, n_y))

    return visited


def checkDistance(visited, people):
    i = 0
    for p in people:
        people[i].append(visited[p[0]-1][p[1]-1]) # 택시와의 최단거리를 4번째 인덱스로 추가
        i += 1

    # 최단거리, 행 번호, 열 번호를 기준 오름차순 정렬
    people.sort(key=lambda x: (-x[4], -x[0], -x[1]))

def solution(X, Y):
    global fuel
    while people:
        visitied = bfs( X-1, Y-1 )
        checkDistance(visitied, people) # 현재 방문한 지점과의 최단거리 탐색
        p_x, p_y, a_x, a_y, dist1 = people.pop() # dist1은 사람과의 최단거리

        for temp in people:
            temp.pop()

        visitied = bfs(p_x-1, p_y-1)
        dist2 = visitied[a_x-1][a_y-1] 
        X, Y = a_x, a_y

        if dist1 == -1 or dist2 == -1:
            print(-1)
            return

        fuel -= dist1
        if fuel < 0:
            break

        fuel -= dist2
        if fuel < 0:
            break

        fuel += dist2 * 2

    if fuel < 0: # 목적지 도달하지 못하고 연료가 떨어지면
        print(-1)
    else:
        print(fuel)


solution(X, Y)
