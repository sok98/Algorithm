import sys
input = sys.stdin.readline

N = int(input())

def solution(N):
    count = 0

    hh = [ i for i in [3, 13, 23] if i<=N]
    mns = [3, 13, 23, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 43, 53]

    for h in range(N+1):
        for m in range(60):
            for s in range(60):
                if '3' in str(h)+str(m)+str(s):
                # if (h in hh) or (m in mns) or (s in mns): 
                    count += 1
    print(count)

solution(N)
# solution(5) # 11475