# [silver-4] 1244 스위치 켜고 끄기
# algorithm 구현, 시뮬레이션
# 메모리: 	KB
# 시간:     ms

import sys
input = sys.stdin.readline

N = int(input())

switches = [-1]
student = {}
switches += (list(input().split()))
    
S = int(input())
for i in range(1, S+1):
    s, c = map(int, input().split())
    student[s] = c

# 남학생 스위치
for i in range(student[1], N+1, student[1]):
    if switches[i]=='0':
        switches[i] = '1'
    else:
        switches[i] = '0'

result = ' '.join(switches[1:])
print(result)

# 여학생 스위치
for i in range(N+1):
    if i ==0:
        if switches[student[2]-i]=='0':
            switches[student[2]-i] = '1'
        else:
            switches[student[2]-i] = '0'
        continue

    if student[2]-i<1:
        break

    if switches[student[2]-i] == switches[student[2]+i]:
        if switches[student[2]-i]=='0':
            switches[student[2]-i] = '1'
        else:
            switches[student[2]-i] = '0'

        if switches[student[2]+i]=='0':
            switches[student[2]+i] = '1'
        else:
            switches[student[2]+i] = '0'

result = ' '.join(switches[1:])
print(result)