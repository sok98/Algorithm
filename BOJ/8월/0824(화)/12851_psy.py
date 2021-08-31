# [gold-5] 12851 숨바꼭질 2 (다시 풀기)
# algorithm  BFS
# 메모리:    226652 KB
# 시간:      5712 ms

import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int,input().split()) # 수빈 / 동생

def q():
    dp = deque([(K, 0)])

    while dp:
        position, count = dp.popleft()
        # 목적지 도착
        if position == N:
            if  N in dp:
                answer = dp.count(N)*2
            else:
                answer = 2
            return count, answer

        dp.append((position-1, count+1))
        dp.append((position+1, count+1))
        # 2로 나눈 몫 만큼 이동
        if position % 2 == 0:
            dp.append((position // 2, count+1))
        
print(*q(), sep="\n")
    
    




