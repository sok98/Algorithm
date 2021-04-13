import sys
input = sys.stdin.readline

N = int(input())

step = [0 for _ in range (N+3)]
value = [0 for _ in range (N+3)]

for i in range(1, N+1):
    value[i]= int(input())

step[1]=value[1]
step[2]=value[1]+value[2]
step[3]=max(value[1]+value[3], value[2]+value[3])

for i in range(4, N+1):
    step[i]=max(step[i-3]+value[i-1]+value[i], step[i-2]+value[i])
    
print(step[N])
