import sys
input = sys.stdin.readline

position = input()

def solution(position):
    row = int(position[1])
    column = int(ord(position[0])-ord('a')) + 1

    # 나이트가 이동할 수 있는 경우의 수
    steps = [(-2, 1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

    result = 0
    for step in steps:
        next_row = row + step[0]
        next_column = column + step[1]

        if next_row >= 1 and next_row<=8 and next_column >= 1 and next_column<=8:
            result += 1
    print(result)
solution(position)
# solution('a1') # 2
# solution('e5') # 8
