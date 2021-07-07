import sys
input = sys.stdin.readline

N = int(input())

def solution(N):
    count = 0
    
    while(N>1):
        if count>=500:
            return -1
        # N이 짝수라면 2로 나눔
        if N%2 ==0:
            N//=2
        # N이 홀수라면 3을 곱하고 1을 더함
        else:
           N = N*3+1
        count+=1
    return count

# print(solution(6)) # 8
# print(solution(16)) # 4
# print(solution(626331)) # -1