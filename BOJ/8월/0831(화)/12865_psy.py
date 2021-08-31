# [gold-5] 12865 평범한 배낭
# algorithm  다이나믹 프로그래밍
# 메모리:    226652 KB
# 시간:      5712 ms

import sys
input = sys.stdin.readline

N, K = map(int,input().split()) # 물품 / 버티는 무게
bag= [ [0]*(K+1) for _ in range(N+1)]

for i in range(1, N+1):
    weight, value = map(int,input().split())

    for j in range(1, K+1):
        if j>=weight:
            bag[i][j] = max(bag[i-1][j], bag[i-1][j-weight]+value)
        else:
            bag[i][j] = bag[i-1][j]

print(bag[N][K])



