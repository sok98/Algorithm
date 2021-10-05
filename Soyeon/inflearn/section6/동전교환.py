import sys
input = sys.stdin.readline

N = int(input())
coin = list(map(int, input().split()))
coin.sort(reverse=True)
tSum = int(input())
count = 10e9

def dfs(L, total):
    global count

    if total == tSum:
        if L<count:
            count = L
    elif total > tSum or L >= count:
        return
    else:
        for i in range(len(coin)):
            dfs(L+1, total+coin[i])

dfs(0, 0)
print(count)
