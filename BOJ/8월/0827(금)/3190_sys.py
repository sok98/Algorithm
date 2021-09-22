from collections import deque
import sys
input = sys.stdin.readline

# 보드 그리기
N = int(input())
board = [[0 for _ in range(N)] for _ in range(N)]

# 사과 위치 표시
K = int(input())
for _ in range(K):
    x, y = map(int, input().split())
    board[x-1][y-1] = -1    # 문제에서 board는 1행 1열부터 시작하기 때문

# curve에 {시간 : 방향} 으로 저장, 방향은 L은 0, D는 1로 표시
L = int(input())
LD = {'L':0, 'D':1}
curve = {}
for _ in range(L):
    x, c = input().split()
    curve[int(x)] = LD[c]


# 0: 북, 1: 동, 2: 서, 3: 남 / [L 적용 방향, D 적용 방향]
dir = {0:[2,1], 1:[0,3], 2:[3,0], 3:[1,2]}
xy = {0:(-1,0), 1:(0,1), 2:(0,-1), 3:(1,0)}
c = 1   # 현재 동쪽을 향함

time = 0
body = deque([[0,0]])
while True:
    time += 1
    x, y = body[-1][0] + xy[c][0], body[-1][1] + xy[c][1]

    # 닿으면 멈추기
    if (x < 0 or y < 0 or x >= N or y >= N) or [x, y] in body:
        print(time)
        break
    
    # 몸 길이 늘린 후, 사과 있으면 먹고 없으면 몸 길이 원상복귀
    body.append([x,y])
    if board[x][y] == -1:
        board[x][y] = 0
    else:
        body.popleft()

    # 시간 됐을 때 방향 바꾸기  
    if time in curve:
        c = dir[c][curve[time]]

