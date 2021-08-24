# [silver-3] 9375 패션왕 신해빈
# algorithm 문자열, 해시
# 메모리: 	 32040 KB
# 시간:      116 ms

import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
clothes = {}
result = []
for _ in range(T):
    N = int(input())

    clothes = {}
    count = 0

    for _ in range(N):
        name, cloth = input().split()
        if cloth not in clothes:
            clothes[cloth] = []
            clothes[cloth].append(name)
        else:
            if name not in clothes[cloth]:
                clothes[cloth].append(name)

    count = 1

    for key, item in clothes.items():
        count*=(len(item)+1)
    result.append(count-1)

for r in result:
    print(r)
