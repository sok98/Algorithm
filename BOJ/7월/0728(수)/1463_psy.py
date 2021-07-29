# [silver-3] 1463 1로 만들기
# algorithm 다이나믹 프로그래밍
# 메모리: 115244KB
# 시간: 840ms


from collections import defaultdict
import sys
input = sys.stdin.readline

N = int(input())
cDic = defaultdict(lambda: 99999)
cDic[0], cDic[1], cDic[2], cDic[3] = 0, 0, 1, 1

if N>3:
    for i in range(4, N+1):
        if i%2 == 0 and i%3==0:
            cDic[i] = min(cDic[i//3], cDic[i//2], cDic[i-1])+1
        elif i%3==0:
            cDic[i] = min(cDic[i//3], cDic[i-1])+1
        elif i%2==0:
            cDic[i] = min(cDic[i//2], cDic[i-1])+1
        else:
            cDic[i] =cDic[i-1]+1

print(cDic[N])