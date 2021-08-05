# [silver-3] 9095 1, 2, 3 더하기
# algorithm 다이나믹 프로그래밍
# 메모리: 	29200KB
# 시간: 76ms

T = int(input())

nList = [0, 1, 2, 4]
result = []

for _ in range(T):
    n = int(input())
    for i in range(len(nList), n+1):
        nList.append(nList[i-1] + nList[i-2] + nList[i-3])
    result.append(nList[n])

for r in result:
    print(r)