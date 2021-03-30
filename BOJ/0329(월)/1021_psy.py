import collections as col

n, m =map(int, input().split())
nums = list(map(int, input().split()))

dp = col.deque(range(1, n+1))
answer=0

for i in nums:
    if dp[0] == i:
        dp.popleft()
        continue
    if dp.index(i) < len(dp) - dp.index(i): #deque하려는 인덱스가 더 왼쪽에 있으면
        while dp[0] != i: #왼쪽으로 
            dp.rotate(-1)
            answer+=1
    else:
        while dp[0] != i: #오른쪽으로
            dp.rotate(1)
            answer+=1
print(answer)

