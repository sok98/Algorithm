# [Weekly Chanllenge] 입실 퇴실
# 획득 포인트 7

from collections import deque

def solution(enter, leave):
    answer = [0 for _ in range(len(enter))]
    room = []

    enter = deque(enter)
    leave = deque(leave)

    for e in enter:
        for r in room: # 대기실에 있는 사람들의 만난 횟수 +1
            answer[r-1] += 1
        answer[e-1] += len(room) # 본인을 제외한 현재 대기실의 인원 만큼 만남
        room.append(e) # 대기실 입장

        while leave and leave[0] in room: # leave에 첫번째 사람을 room에서 제거 
            room.remove(leave.popleft())

    return answer