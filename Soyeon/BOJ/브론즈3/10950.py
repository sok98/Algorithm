# A+B - 3

N = int(input())

result = []

for i in range(N):
    a, b = map(int, input().split())
    result.append(a+b)

for r in result:
    print(r)