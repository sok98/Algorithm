# [silver-1] 1927 최소힙
# algorithm  자료구조, 우선순위 큐
# 메모리:    35124 KB
# 시간:      192 ms

import sys
import heapq as hp
input = sys.stdin.readline

tree = []
result = []
count = 0
N = int(input())

for _ in range(N):
    x = int(input())

    if x==0:
        if len(tree)<=0:
            result.append(0)
        else:
            result.append(hp.heappop(tree))
        count += 1
    else: # 자연수면 heap에 추가
        hp.heappush(tree, x)

for i in range(count):
    try:
        print(result[i])
    except IndexError:
        print(0)   