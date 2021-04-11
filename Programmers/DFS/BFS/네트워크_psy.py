def dfs(i,n, computers, visited):
    visited[i] = True 

    for j in range(n):  
        if computers[i][j] == 1 and i!=j and visited[j] == False:
            dfs(j, n, computers,visited)

def solution(n, computers):
    answer = 0
    # 방문 노드 만들기
    visited = [False]*n

    # dfs 재귀함수로 탐색
    for idx in range(n):
        if visited[idx] == False:
            dfs(idx, n, computers, visited)
            answer += 1 

    return answer