# [silver-5] 11651 죄표 정렬하기 2
# algorithm  정렬
# 메모리:   51272 KB
# 시간:     408 ms

import sys
input = sys.stdin.readline

N = int(input())
result = []

for i in range(N):
    a, b = map(int, input().split())
    result.append((a, b))

for r in sorted(result, key=lambda num: (num[1], num[0])):
    print(*r)
