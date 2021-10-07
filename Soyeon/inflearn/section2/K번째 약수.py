import sys

#sys.stdin=open("input.txt", "rt")

input = sys.stdin.readline
n, k = map(int, input().split())

nums = []

for i in range(1, n+1):
    if n%i==0:
        nums.append(i)

nums.sort()
# print("nums", nums)


if len(nums)<k:
    print(-1)
else:
    print(nums[k-1])