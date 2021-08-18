# [silver-3] 1966 프린터 큐
# algorithm  구현, 자료 구조, 시뮬레이션, 큐
# 메모리:    31780 KB
# 시간:      112 ms

import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

result = []

for _ in range(T):
    N, M = map(int, input().split())
    document = deque([int(x) for x in input().split()])
    priority = 1
    
    while(document):
        if document[0] == max(document) and M==0:
            result.append(priority)
            break
        elif document[0] == max(document):
            document.popleft()
            priority+=1
            M-=1

        else:
            document.rotate(-1)
            M-=1

        if M<0:
                M+=len(document)
    
        
for r in result:
    print(r)
