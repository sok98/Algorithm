# [silver-3] 9095 1, 2, 3 더하기
# algorithm 
# 메모리: KB
# 시간: ms

T = int(input())

nList = [0, 1, 2, 4]
result = []

for _ in range(T):
    n = int(input())

    for i in range(4, n+1):
        nList.append(nList[i-1] + nList[i-2] + nList[i-3])
    result(nList[n])