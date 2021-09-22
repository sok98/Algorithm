# [gold-5] 1011 Fly me to the Alpha Centauri
# algorithm 수학
# 메모리:   29200 KB
# 시간:     1596 ms

result = []

T = int(input())
for i in range(T):
    a, b = map(int, input().split())
    distance = b-a
    num = 1
    
    while True:
        if num ** 2 <= distance < (num + 1) ** 2:
            break

        num += 1
    if num ** 2 == distance:
        result.append((num * 2) - 1)
    elif num ** 2 < distance <= num ** 2 + num:
        result.append(num * 2)
    else:
        result.append((num * 2) + 1)

for r in result:
    print(r)
