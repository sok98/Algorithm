# [blonze-2] 2231 분해합
# algorithm 브루트포스
# 메모리: 28776KB
# 시간: 68ms

import sys
input = sys.stdin.readline

# 첫째 줄에 자연수 N(1 ≤ N ≤ 1,000,000)이 주어진다.

N = int(input())
numStr = str(N) # 216 -> '216'
start = N-(int(numStr[0])+(len(numStr)-1)*9) # target num이 216면 start를 216-(2+9+9) = 196 부터

def minCtor(N):
    result = 0

    for num in range(start, N):
        subSum = 0
        numStr = str(num)

        # 각 자릿수 합 subSum
        for j in range(len(numStr)):
            subSum += int(numStr[j])

        # num이 ctor의 생성자이면
        ctor = num + subSum
        if ctor == N:
            result = num
            print(result)
            return
    print(result)
minCtor(N)