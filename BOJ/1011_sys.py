T = int(input())
answer = []
for i in range(T):
    x, y = map(int, input().split())
    i = 0
    sum = 0
    while True:
        if y - x <= 1 + sum:
            answer.append(i + 1)
            break
        i += 1
        sum += i

for i in answer:
    print(i)
