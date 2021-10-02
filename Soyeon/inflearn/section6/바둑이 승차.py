import sys
input = sys.stdin.readline

C, N = map(int, input().split())
dogs = [ int(input()) for _ in range(N) ]
max = 0

def dfs(l, total):
    global max

    if total > C: # 총 합이 C를 넘으면 중단
        return

    if l == N:
        if total > max:
            max = total
    else:
        dfs(l+1, total+dogs[l])
        dfs(l+1, total)

if sum(dogs) <= C:
        max = sum(dogs)
else:
    dfs(0, 0)

print(max)