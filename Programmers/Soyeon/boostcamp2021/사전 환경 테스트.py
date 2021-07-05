def solution(v):
    answer = []
    x = {}
    y = {}
    
    for i in v:
        if i[0] in x:
            x[i[0]] +=1
        else:
            x[i[0]] = 1
        
        if i[1] in y:
            y[i[1]] += 1
        else:
            y[i[1]] = 1
            
    for key, value in x.items():
        if value <2:
            answer.append(key)
            
    for key, value in y.items():
        if value <2:
            answer.append(key)


    print(answer)

    return answer