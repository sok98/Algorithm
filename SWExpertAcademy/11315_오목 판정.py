# 테케 66개 통과
# 오목이 아닌 빙고를 구현함 ㅋㅋㅋ
# N이 6이상일 때 한 줄이 아닌 연속된 5개의 o만 나오면 됨

import sys
input = sys.stdin.readline

T = int(input())
answer = []

# 줄의 갯수
for test_case in range(1, T+1):
    #print("----------")
    N = int(input())
    
    board = [input().rstrip() for _ in range(N)]

    h, v, l, r = False, False, True, True
    vv = [True for _ in range(N)]
    
    rock =""
    for _ in range(N):
        rock+="o"

    #print("rock", rock)

    for i in range(N):
        
        # 가로
        #print("board[i] & rock", board[i], rock)
        if board[i] == rock:
            #print("SAME!!!!")
            h = True

        # 세로
        for k in range(N):
            if board[i][k:k+1] == "o":
                vv[k] = (vv[k] and True)
            else:
                vv[k] = False

        # 대각선(왼)
        if board[i][i:i+1] == ".":
            # print("왼", board[i][i:i+1])
            l = l and False

        # 대각선(오)
        if board[i][N-i-1:N-i] == ".":
            r = r and False


    # 세로 체크
    #print("vv", vv)
    if True in vv:
            v = True

    #print(h, v, l, r)

    if (h or v or l or r) is True:
        answer.append(f"#{test_case} YES")
    else:
        answer.append(f"#{test_case} NO")

for asw in answer:
    print(asw)

