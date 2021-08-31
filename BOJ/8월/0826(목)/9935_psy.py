# [gold-4] 9935 문자열 폭발 (시간초과)
# algorithm  자료구조
# 메모리:     KB
# 시간:       ms

import sys
input = sys.stdin.readline

l = input().rstrip('\n')
b = input().rstrip('\n')


# 시간 초과
def solution(l, b):
    before = []
    line = list(l)
    bomb = list(b)

    while len(line)>=len(bomb): # 남은 문자열이 더 길 때
        for i in range(len(line)):
            try:
                if line[i] == bomb[0]: # 첫 문자열이 일치하면
                    same = True
                    for j in range(len(bomb)):
                        if  line[i+j] != bomb[j]:
                            same = False
                    
                    if same:
                        for _ in range(len(bomb)):
                            line.pop(i)

            except IndexError:
                break

        if before == line:
            break
        else:
            before = line
    if len(line)>0:
        print(''.join(line))
    else:
        print("FRULA")
    return

solution('12ab112ab2ab', '12ab')  
solution('mirkovC4nizCC44', 'C4')



# 시간 초과
# def solution(line, bomb):
#     before = ''
#     stacks = [[] for _ in range(len(bomb)-1)]

#     while line:
#         if line.find(bomb)>=0:
#             end = line.find(bomb) + len(bomb)-1
#             start = line.find(bomb)
#             lList = list(line)
#             for i in range(end, start-1, -1):
#                 lList.pop(i)
#             line = ''.join(lList)

#         if before == line:
#             print(line)
#             return
#         else:
#             before = line

#     print("FRULA")
# solution(line, bomb)

# 시간초과
# def solution(line, bomb):
#     before = ''

#     while line:
#         line = line.replace(bomb, '')

#         if before == line:
#             print(line)
#             return
#         else:
#             before = line

#     print("FRULA")



# solution('mirkovC4nizCC44', 'C4') # mirkovniz
# solution('12ab112ab2ab', '12ab') # FRULA