from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 5)
input = stdin.readline


def rotate(graph, x, y, l):
    k = 2 ** l
    n = len(graph)
    for x in range(0, n, k):
        for y in range(0, n, k):
            tmp = [graph[i][y:y + k] for i in range(x, x + k)]
            for i in range(k):
                for j in range(k):
                    graph[x + j][y + k - 1 - i] = tmp[i][j]


def max_area_count(graph, r, c):
    length = len(graph)
    ret = 1
    graph[r][c] = 0

    for dr, dc in dir:
        nr, nc = r + dr, c + dc
        if 0 <= nr < length and 0 <= nc < length and graph[nr][nc] > 0:
            ret += max_area_count(graph, nr, nc)

    return ret


def solution(L, length):
    for l in L:
        rotate(graph, 0, 0, l)

        ## 주변 얼음 개수 카운팅
        need_minus = []
        for r in range(length):
            for c in range(length):
                if graph[r][c] <= 0:
                    continue

                count = 0
                for dr, dc in dir:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < length and 0 <= nc < length and graph[nr][nc]:
                        count += 1

                if count < 3:
                    need_minus.append((r, c))

        for r, c in need_minus:
            graph[r][c] -= 1

    print(sum(sum(ar) for ar in graph))
    # 제일 큰 덩어리
    ans = 0
    for x in range(length):
        for y in range(length):
            if graph[x][y] > 0:
                ans = max(ans, max_area_count(graph, x, y))
    print(ans)


N, Q = map(int, input().split())
graph = []
for i in range(2 ** N):
    graph.append(list(map(int, input().split())))

L = list(map(int, input().split()))
dir = [(1, 0), (0, -1), (0, 1), (-1, 0)]
solution(L, len(graph))
