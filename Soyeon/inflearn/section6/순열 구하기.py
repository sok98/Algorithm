import sys
input = sys.stdin.readline

N, M = map(int, input().split())
res = [0]*N
ch = [0]*(N+1)
count=0

def dfs(L):
    global count

    if L==M:
        for j in range(L):
            print(res[j], end=" ")
        print()
        count+=1
    else:
        for i in range(1, N+1):
            if ch[i]==0:
                ch[i]=1 # 체크
                res[L]=i
                dfs(L+1)
                ch[i]=0 # 되돌아 왔을 때 체크 취소

dfs(0)
print(count)