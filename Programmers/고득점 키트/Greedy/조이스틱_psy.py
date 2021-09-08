# 테스트 케이스 5, 11 실패
import string
ZAZAAZ 345
def solution(name):
    
    answer = 0
    back_distance=0
    alpha = list(string.ascii_uppercase)

    # 단어 위 아래 ▲▼
    for c in range(len(name)):
        distance = alpha.index(name[c]) - alpha.index('A')
        reverse_distance = abs(alpha.index(name[c]) - alpha.index('Z')-1)
        
        #순열 역순열 중 min 값을 sum
        answer += min([distance, reverse_distance])

     # 단어의 길이 ◀ ▶
    reversed_name = ''.join(reversed(name)) 
    print("reversed_name>> ", reversed_name)
    total_distance =[]

    if 'A' in name:  # 'A'를 포함한 경우
        # 'A'까지의 거리가 더 가까운 방향을 먼저 탐색
        # 순방향 탐색
        for i in range(name.find('A'),len(name)): #가장 가까운 A문자열의 end index 찾기 ZAAZZZAZZ
            if name[i] != 'A':
                end_index = i
                break
        tail_length = len(name[end_index:]) # 방향을 바꾸지 않은 길이
        back_distance = 2*(name.find('A')-1) #방향을 바꾼 부분의 길이
        total_distance.append(tail_length + back_distance)
        print("tail_length>> ", tail_length)
        print("back_distance>> ", back_distance)
        print()

        # 역방향 탐색
        for i in range(reversed_name.find('A'),len(reversed_name)):
            if reversed_name[i] != 'A':
                end_index = i
                break
        tail_length = len(reversed_name[end_index:])
        back_distance = 2*(reversed_name.find('A')-1)  + 1 #역방향은 뒤로 가는 횟수 1 포함
        total_distance.append(tail_length + back_distance)
        print("tail_length>> ", tail_length)
        print("back_distance>> ", back_distance)
    else: # 'A'를 포함하지 않은 경우
        total_distance.append(len(name)-1)
    print()
    print("alpha up down>> ", answer)
    print("total_distance>> ", total_distance)
    answer+=min(total_distance) # ▲▼ + min(◀ ▶)

    print("answer>> ", answer)
    return answer

#가장 가까운 A문자열의 end index 찾기 (부분해)
# def find_end(name):
#     answer = name.find('AA')
#     for i in range(name.find('AA'),len(name)):
#         if name[i] != 'A':
#             end_index = i
#             break
#     print("tail_length>> ", len(name[end_index:]))
#     print("end_index>> ", end_index)
#     print("answer>> ", answer)
#     return answer
#solution22("JJAAAAJJAAJJJ")
