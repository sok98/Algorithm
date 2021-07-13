N, M = map(int, input().split())

coins = [int(input()) for _ in range(N)]

# 한 번 계산된 결괄르 저장하기 위한 DP 테이블 초기화
d = [10001]*(M+1)

# 다이나믹 프로그래밍(Dynamic Programming) 진행(바텀업)
d[0] = 0
for i in range(N):
    for j in range(coins[i], M+1):
        if d[j-coins[i]] != 10001:
            d[j] = min(d[j], d[j-coins[i]]+1)

# 계산된 결과 출력
if d[M] == 10001:
    print(-1)
else:
    print(d[M])
