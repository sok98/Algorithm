# [silver-2] 9465 스티커
# algorithm  다이나믹 프로그래밍
# 메모리:    45396 KB
# 시간:      1092 ms

import sys
input = sys.stdin.readline

T = int(input())
result = []

for _ in range(T):
    N = int(input())

    stickers = [list(map(int, input().split())) for _ in range(2)]

    if N==1:
        print(max(stickers[0][0], stickers[1][0]))
        continue

    # 1열
    stickers[0][1] = stickers[0][1] + stickers[1][0]
    stickers[1][1] = stickers[1][1] + stickers[0][0]

    for k in range(2, N): # 바로 전 or 2번째 전 열의 값 중 최댓 값을 현재의 값과 더해서 갱신 
        stickers[0][k] = stickers[0][k] + max(stickers[1][k - 1], stickers[1][k - 2])
        stickers[1][k] = stickers[1][k] + max(stickers[0][k - 1], stickers[0][k - 2])

    result.append(max(stickers[0][N-1], stickers[1][N-1]))

for r in result:
    print(r)
