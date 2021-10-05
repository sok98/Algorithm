import sys
input = sys.stdin.readline

# N, M = map(int, input().split())
# # 0: 북 / 1: 동 / 2: 남 / 3: 서
# x, y, d = map(int, input().split())
dic = {0: (0, 1), 1: (1, 0), 2:(0, -1), 3:(-1, 0)}

# # 0: 육지 / 1: 바다
# arr = [ [0]*M for _ in range(N)]

def solution(N, M, x, y, d, arr):
    move, count = 0, 0

    while True:
        for _ in range(4):
            # 맵을 벗어나지 않음
            if x+dic[d][0]<M and x+dic[d][0]>=0 and y+dic[d][1] >= 0 and y+dic[d][1] < N:
                # 이동하려는 위치가 육지(0)일 때
                if arr[x+dic[d][0]][y+dic[d][1]] == 0:
                    x += dic[d][0]
                    y += dic[d][1]
                    move += 1
                    exit
        print(move)
        exit
    
solution(4, 4, 1, 1, 0, [[1, 1, 1, 1], [1, 0, 0, 1], [1, 1, 0, 1], [1, 1, 1, 1]])


