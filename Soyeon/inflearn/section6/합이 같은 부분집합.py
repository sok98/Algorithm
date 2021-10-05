# [section-6] 합이 같은 부분집합

import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

result = False
def dfs(l, sum): # l은 인덱스 번호, sum은 부분집합의 합
  if l == N: # 리프 노드의 레벨이 되면 합 계산
    if sum == (total-sum):
      print("YES")
      sys.exit(0) # 프로그램 전체 종료
  elif sum<=(total//2): # sum이 총합의 반을 넘으면 탐색할 필요 X
    dfs(l+1, sum)         # num[l]을 사용 X
    dfs(l+1, sum+nums[l]) # num[l]을 사용 O

total = sum(nums)
dfs(0, 0)
print("NO")

