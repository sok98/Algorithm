# [gold-4] 17779 게리맨더링 2
# algorithm 구현 
# 메모리:   29200 KB
# 시간:     924  ms

import sys
input = sys.stdin.readline


def A(x, y, d1, d2):

    # 5번 표시
    ground = [[0 for _ in range(N+1)] for _ in range(N+1)]
    ground[x][y] = 5
    for i in range(1, d1+1):
        ground[x+i][y-i] = 5
        ground[x+d2+i][y+d2-i] = 5
    for i in range(1, d2+1):
        ground[x+i][y+i] = 5
        ground[x+d1+i][y-d1+i] = 5

    # 1번 선거구: 1 ≤ r < x+d1, 1 ≤ c ≤ y
    region1 = 0
    for r in range(1, x+d1):
        for c in range(1, y+1):
            if ground[r][c] == 5:
                break
            region1 += matrix[r][c]

    # 2번 선거구: 1 ≤ r ≤ x+d2, y < c ≤ N
    region2 = 0
    for r in range(1, x+d2+1):
        for c in range(N, y, -1):
            if ground[r][c] == 5:
                break
            region2 += matrix[r][c]


    # 3번 선거구: x+d1 ≤ r ≤ N, 1 ≤ c < y-d1+d2
    region3 = 0
    for r in range(x+d1, N+1):
        for c in range(1, y-d1+d2):
            if ground[r][c] == 5:
                break
            region3 += matrix[r][c]


    # 4번 선거구: x+d2 < r ≤ N, y-d1+d2 ≤ c ≤ N
    region4 = 0
    for r in range(x+d2+1, N+1):
        for c in range(N, y-d1+d2-1, -1):
            if ground[r][c] == 5:
                break
            region4 += matrix[r][c]


    region5 = total - (region1+region2+region3+region4)
    max_val = max(region1, max(region2, max(region3, max(region4, region5))))
    min_val = min(region1, min(region2, min(region3, min(region4, region5))))
    return max_val - min_val

N = int(input())
matrix = [[0]*(N+1)]

for _ in range(N):
    lst = [0]
    number = list(map(int, input().split()))
    lst.extend(number)
    matrix.append(lst)

total = 0
for y in range(1, N+1):
    for x in range(1, N+1):
        total += matrix[y][x]

answer = 10**9
for x in range(1, N+1):
    for y in range(1, N+1):
        for d1 in range(1, N+1):
            for d2 in range(1, N+1):
                if x+d1+d2 > N or y-d1 < 1 or y+d2 > N:
                    continue

                answer = min(answer ,A(x, y, d1, d2))

print(answer)