import sys
input = sys.stdin.readline

N, M = map(int, input().split())
list = list(map(int, input().split()))

start = 0
end = max(list)
result = 0

while start<=end:
    mid = (start+end)//2
    sum = 0

    for item in list:
        if item>mid:
            sum += (item-mid)
    if sum < M:
        end = mid - 1
    else:
        result = mid # 최대한 덜 잘랐을때가 정답이므로, result에 기록
        start = mid + 1

print(result)
