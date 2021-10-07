import sys
#input = sys.stdin

N, M = map(int, input().split())
graph = [ list(map(int, input())) for _ in range(N)]

print("graph =", graph)

# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x, y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x>= N or y <= -1 or y >= M:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        # 해당 노드를 방문 처리
        graph[x][y] = 1
        # 상하좌우의 다른 노드를 방문
        dfs(x-1, y) # 상
        dfs(x+1, y) # 하
        dfs(x, y-1) # 좌
        dfs(x, y+1) # 우
        return True
    return False

# 모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(N):
    for j in range(M):
        # 현재 위치에서 DFS 수행
        if dfs(i, j) == True:
            result+=1
print("result =", result)