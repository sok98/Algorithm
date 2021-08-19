# [silver-4] 1676 팩토리얼 0의 개수
# algorithm  수학
# 메모리:   29200 KB
# 시간:     80 ms

import sys
input = sys.stdin.readline

T = int(input())
result, count = 1, 0

for i in range(1, T+1):
    result*=i

for idx in range(str(result).rfind('0'), -1, -1):
    if str(result)[idx] != '0':
        break
    count += 1

    
print(count)

#print(str(result).count('0'))