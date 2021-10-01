import sys
input = sys.stdin.readline

N, K = map(int, input().split())

def solution(N, K):
    count = 0

    while N>1:
        if N%K==0:
            N//=K
        else:
            N-=1
        count+=1
    print("count =", count)
    

solution(N, K)
# solution(25, 5) # 2
# solution(25, 3) # 6