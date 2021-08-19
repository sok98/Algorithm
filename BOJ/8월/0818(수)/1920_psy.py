# [silver-4] 1920 수 찾기
# algorithm  이분 탐색
# 메모리:    44724 KB
# 시간:      652 ms

import sys
input = sys.stdin.readline

N = int(input())
nn = sorted([int(x) for x in input().split()])
M = int(input())
mn = [int(x) for x in input().split()]

result = []

def binary_search(array, target, start, end):
    while start<=end:
        mid = (start+end)//2
        # 찾은 경우 중간점 인덱스 반환
        if array[mid]==target:
            return 1
        elif array[mid]>target:
            end = mid-1
        else:
            start = mid+1
    return 0

for num in mn:
    result.append(binary_search(nn, num, 0, len(nn)-1))

for r in result:
    print(r)
