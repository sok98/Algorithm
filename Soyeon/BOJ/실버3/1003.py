# [silver-3] 1003 피보나치 함수
# algorithm 다이나믹 프로그래밍
# 메모리: 	29200 KB
# 시간:     76 ms

T = int(input())
result = []

for _ in range(T):
    N = int(input())
    zero = [1, 0, 1]
    one = [0, 1, 1]
    if N >= 3:
        for i in range(3, N+1):
            zero.append(zero[i-1]+zero[i-2])
            one.append(one[i-1]+one[i-2])
    result.append((zero[N], one[N]))

for r in result:
    print(*r)
