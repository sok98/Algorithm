# [blonze-1] 2839 설탕 배달
# algorithm 다이나믹 프로그래밍, 그리디, 브루트포스
# 메모리: 29200KB
# 시간: 72ms

import sys
input = sys.stdin.readline

N = int(input())

bag = [ 9999 for _ in range(N+1)]
bag[3] = 1

if N>=5:
    bag[5] = 1


for i in range(4, N+1):
    if i==3 or i==5:
        continue

    if i<5:
        bag[i] = bag[i-3]+1
    else:
        bag[i] = min(bag[i-3], bag[i-5]) + 1

if bag[N] >= 9999:
    print(-1)
else:
    print(bag[N])
