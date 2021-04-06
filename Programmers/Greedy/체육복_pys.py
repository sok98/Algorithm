def solution(n, losts, reserves):
    reserve = set(reserves) - set(losts) # 진짜 여벌 있는 학생들만 남기기
    lost = set(losts) - set(reserves)
    
    for r in reserve:
        if r-1 in lost: # 잃어버린 사람이면....
            lost.remove(r-1)
        elif r+1 in lost:
            lost.remove(r+1)
    
    return n - len(lost)


# 테스트 케이스 11 통과 못함
# def solution(n, lost, reserve):
#     answer = []
#     count_lost=list(set(lost)-set(reserve))
#     count_reserve=list(set(reserve)-set(lost))
    
#     for i in count_lost:
#         if (len(count_lost)==0)or(len(count_reserve)==0):
#             break
#         else:
#             if i-1 in count_reserve:
#                 count_reserve.remove(i-1)
#                 count_lost.remove(i)
#             elif i+1 in count_reserve:
#                 count_reserve.remove(i+1)
#                 count_lost.remove(i)
#     answer.append(n-len(count_lost))
                
#     for i in count_lost:
#         if (len(count_lost)==0)or(len(count_reserve)==0):
#             break
#         else:
#             if i+1 in count_reserve:
#                 count_reserve.remove(i+1)
#                 count_lost.remove(i)
#             elif i-1 in count_reserve:
#                 count_reserve.remove(i-1)
#                 count_lost.remove(i)
                
#     answer.append(n-len(count_lost))
#     print(answer)
#     return max(answer)
