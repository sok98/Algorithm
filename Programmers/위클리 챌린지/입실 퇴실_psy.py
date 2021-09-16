# [Weekly Chanllenge] 입실 퇴실
# 획득 포인트 7

from collections import deque

def solution(enter, leave):
    answer = [0 for _ in range(len(enter))]
    room = []

    enter = deque(enter)
    leave = deque(leave)

    for i in enter:
        for r in room:
            answer[r-1] += 1
        answer[i-1] += len(room)
        room.append(i)

        while leave and leave[0] in room:
            room.remove(leave.popleft())

    return answer