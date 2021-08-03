# 평균

N = int(input())

rScores = list(map(int, input().split()))
fScores = []

M = max(rScores)

print("rScores", rScores)

for s in rScores:
    fScores.append((s/M)*100)

print("fScores", fScores)
print(sum(fScores)/N)