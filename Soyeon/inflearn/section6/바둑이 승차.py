import sys
input = sys.stdin.readline

C, N = map(int, input().split())
dogs = [ int(input()) for _ in range(N) ]
max = 0

def dfs(l, sum, tsum):
    global max
    
    if sum+(total-tsum) < max: # 계속 탐색해봤자 max가 더 큼
        return

    if sum > C: # 총 합이 C를 넘으면 중단
        return

    if l == N:
        if sum > max:
            max = sum
    else:
        dfs(l+1, sum+dogs[l], tsum+dogs[l])
        dfs(l+1, sum, tsum+dogs[l])
  
total = sum(dogs)
dfs(0, 0, 0)
print(max)