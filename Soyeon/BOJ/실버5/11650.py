# [silver-5] 11650 죄표 정렬하기
# algorithm  정렬
# 메모리:   51272 KB
# 시간:     4360 ms

N = int(input())
result = []

for i in range(N):
    a, b = map(int, input().split())
    result.append((a, b))

for r in sorted(result, key=lambda num: (num[0], num[1])):
    print(*r)
