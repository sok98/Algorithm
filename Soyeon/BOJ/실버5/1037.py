# [silver-5] 1037 약수
# algorithm  수학
# 메모리:   29200	KB
# 시간:     80ms

N = int(input())

nums = list(map(int, input().split()))
nums.sort()

if len(nums)%2!=0:
    print(nums[len(nums)//2]**2)
else:
    print(nums[len(nums)//2-1]*nums[len(nums)//2])

# print(5//2) # 버림, 몫
# print(5/2) # 나누기