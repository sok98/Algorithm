def solution(participant, completion):
    answer = ''
    dic = {}
    
    # participant를 key에 넣고 인원을 value로 카운트
    for p in participant:
        if p in dic:
            dic[p]+=1
        else:
            dic[p]=1
    
    # completion이 있을 때 마다 value--
    for c in completion:
        dic[c]-=1
        
    # value가 0이 아닌 key를 리턴
    for key, value in dic.items():
        if value>0:
            answer = key
            break
    
    return answer