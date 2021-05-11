from itertools import combinations
answer = 0
n, s = map(int, input().split())
li = list(map(int, input().split()))
for i in range(1, n+1):
    clist = list(combinations(li, i))
    for c in clist:
        if sum(c) == s:
            answer += 1

print(answer)