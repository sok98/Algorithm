import sys
input = sys.stdin.readline

N = int(input())
listN = set(map(int, input().split()))

M = int(input())
listM = list(map(int, input().split()))

result=""
for i in listM:
    if i in listN:
        result+="yes "
    else:
        result+="no "

print(result.rstrip())
