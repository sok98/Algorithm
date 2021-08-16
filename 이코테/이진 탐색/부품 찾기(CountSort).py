import sys
input = sys.stdin.readline


N = int(input())
array = [0] * 1000001
listN = list(map(int, input().split()))

for i in listN:
    array[i] = 1

M = int(input())
listM = list(map(int, input().split()))

result=""
for i in listM:
    if array[i] == 1:
        result+="yes "
    else:
        result+="no "

print(result.rstrip())
