from collections import deque

N, M = map(int, input().split())
graph = [ list(map(int, input())) for _ in range(N)]

# 이동할 네 방향 정의(상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

#BFS
def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 네 방향으로 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            # 벽인 경우 무시
            if graph[nx][ny] == 0:
                continue
            elif graph[nx][ny] == 1:
                # 해당 노드를 처음 방문하는 경우에만 최단 거리 등록
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    # 가장 오른쪽 아래까지의 최단거리 반환
    return graph[N-1][M-1]

# BFS를 수행한 결과 출력
print(bfs(0, 0))