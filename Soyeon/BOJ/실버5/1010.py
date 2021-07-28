import sys
input = sys.stdin.readline

answers = []
dic = {}

def factorial(num):
    if num <2:
        return 1

    if "num" in dic:
        return dic[num]
    else:
        dic[num] = num * factorial(num-1)
        return dic[num]

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    result = factorial(M)//(factorial(M-N)*factorial(N))
    answers.append(result)

for answer in answers:
    print(answer)
