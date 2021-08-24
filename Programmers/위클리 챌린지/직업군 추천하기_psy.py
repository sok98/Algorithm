# [Weekly Chanllenge] 직업군 추천하기
# 획득 포인트 4

from collections import defaultdict

def solution(table, languages, preference):
    groups = defaultdict(int)
    
    for t in table:
        temp = list(map(str, t.split()))
        tl = temp[1:]
        tl.reverse()
        for i in range(len(languages)):
            if languages[i] in tl:
                groups[temp[0]] += (tl.index(languages[i])+1)*preference[i]
    max = 0
    gLan =[]
    for key, value in groups.items():
        if value > max:
            gLan = [key]
            max = value
        elif value == max:
            gLan.append(key)
            
    return sorted(gLan)[0]