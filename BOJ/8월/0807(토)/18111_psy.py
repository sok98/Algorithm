# [silver-3] 18111 마인크래프트 (시간초과)
# algorithm 구현, 시뮬레이션
# 메모리: 	KB
# 시간:     ms

import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())
bDic = {}
minTime = 1e9
resultHeight  = 0

ground = [ list(map(int, input().split())) for _ in range(N)]
minNum = min(map(min,ground))
maxNum = max(map(max,ground))

for i in range(minNum,maxNum+1):
    plusCount = 0
    minusCount = 0
    for j in range(N):
        for k in range(M):
            height = ground[j][k] - i
            if height>0:
                #1번 작업 수
                minusCount += height
            elif height<0:
                #2번 작업 수
                plusCount -= height
    if minusCount+B>=plusCount:
        time = minusCount*2 + plusCount
        #계속 비교 => 최솟값
        if minTime >= time:
            minTime = time
            resultHeight = i

print(minTime,resultHeight)
