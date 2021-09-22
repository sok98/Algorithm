# [silver-4] 1021 회전하는 큐
# algorithm  자료구조
# 메모리: 	 32040 KB
# 시간:      92 ms

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
popNums = deque(list(map(int, input().split())))
nums = deque([i for i in range(N)])

for i in range(len(popNums)):
    popNums[i]-=1
count = 0

while(popNums):
    target = (list(nums)).index(popNums[0])
    if target != 0:
        if len(nums)-target < target:
            nums.rotate(1)
        else:
            nums.rotate(-1)
        count+=1

    else:
        nums.popleft()
        popNums.popleft()

print(count)
