# [silver-4] 1244 스위치 켜고 끄기
# algorithm 구현, 시뮬레이션
# 메모리: 	29200 KB
# 시간:     80 ms

# 0 1 0 1 0 0 0 1

import sys
input = sys.stdin.readline

N = int(input())

switches = [-1]
change = {0:1, 1:0}
switches += (list(map(int, input().split())))
    
S = int(input())
for _ in range(S):
    gender, index = map(int, input().split())

    # 남학생 스위치
    if gender == 1:
        for i in range(index, len(switches), index):
            switches[i] = change[switches[i]]

    # 여학생 스위치
    elif gender == 2:
        for i in range(0, len(switches)):
            if i == 0:
                switches[index] = change[switches[index]]
                continue

            if index-i<1 or len(switches)<=index+i:
                break

            if switches[index-i] == switches[index+i]:
                switches[index-i] = change[switches[index-i]]
                switches[index+i] = change[switches[index+i]]
            else:
                break

for i in range(1, len(switches), 20):
    print(*switches[i:i+20]) # print(* => 리스트 아이템을 공백 문자로 구분지어 출력
