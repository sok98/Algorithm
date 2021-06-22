import sys
import itertools
input = sys.stdin.readline

a = int(input())
arr = []
result = []

# 입력값 받기
for i in range(a):
    arr.append(list(map(int, input().split())))

idx = [i for i in range(a)]

# A 팀 구하기
list_A = set(itertools.combinations(idx, a // 2))
for A in list_A:
    sum_a = 0
    sum_b = 0
    # B 팀 구하기
    B = set(idx) - set(A)

    # 팀 별 점수 연산
    for i, j in itertools.combinations(A, 2):
        sum_a += arr[i][j]
        sum_a += arr[j][i]
    for i, j in itertools.combinations(B, 2):
        sum_b += arr[i][j]
        sum_b += arr[j][i]
    result.append(abs(sum_a - sum_b))

print(min(result))