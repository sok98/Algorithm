import sys
input = sys.stdin.readline

N = int(input())
arr = input().split()

def solution(N, arr):
    x, y = 1, 1

    for i in arr:
        if i == 'L' and y>1 :
            y-=1
        elif i == 'R' and y<N:
            y+=1
        elif i == 'D' and x<N:
            x+=1
        elif i == 'U'  and x>1:
            x-=1
    print(x, y)

solution(N, arr)
# solution(5, ['R', 'R', 'R', 'U', 'D', 'D']) # 3 4