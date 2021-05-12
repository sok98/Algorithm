# [silver-4] 11866 요세푸스 문제0
# algorithm 큐
# 메모리: 32692KB
# 시간: 100ms

import sys
input = sys.stdin.readline
from collections import deque

N, K = map( int, input().split())

def josephus(N, K):
    yList = deque(range(1, N+1))
    result = []
    i=0

    while yList:
        yList.rotate(-(K-1))
        result.append(yList.popleft())

    strResult=str(result)
    print("<"+strResult[1:len(strResult)-1]+">")

josephus(N, K)
