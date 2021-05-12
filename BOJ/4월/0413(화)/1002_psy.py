import sys
import math
input = sys.stdin.readline

N = int(input())
answer=[]

for _ in range(N):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    distance = math.sqrt((x1-x2)**2+(y1-y2)**2) #점과 점 사이 거리

    if distance==0 and r1==r2: # 동심원일 때
        answer.append(-1)
    elif (abs(r1-r2) == distance) or (r1+r2 == distance): # 내접 혹은 외접
        answer.append(1)
    elif abs(r1-r2) < distance < (r1+r2): # 원이 서로 다른 두 점
        answer.append(2)
    else: # 원이 만나지 않음
        answer.append(0)

for i in range(N):
    print(answer[i])
    