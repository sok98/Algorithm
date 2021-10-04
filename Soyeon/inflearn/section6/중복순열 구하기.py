import sys
input = sys.stdin.readline

N, M = map(int, input().split())
res = [0]*(M)
count = 0

def dfs(L):
    global count

    if L == M:
        print(*res)
        count+=1
    else:
        for i in range(1, N+1):
            res[L]=i
            dfs(L+1)

dfs(0)
print(count)
