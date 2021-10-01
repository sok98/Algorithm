N = int(input())

foodList = list(map(int, input().split()))

d = [0]*100

d[0]=foodList[0]
d[1]=max(foodList[0], foodList[1])

for i in range(2, len(foodList)):
    d[i] = max(d[i-2]+foodList[i], d[i-1])

print(d[N-1])