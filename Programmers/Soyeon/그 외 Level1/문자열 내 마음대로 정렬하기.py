def solution(strings, n):
    answer = []
    sortedList = []
    dic = {}
    
    for i in range(len(strings)):
        if strings[i][n:n+1] not in dic:
             dic[strings[i][n:n+1]] = []
        
        sortedList.append(strings[i][n:n+1])
        dic[strings[i][n:n+1]].append(strings[i])
                   
    sortedList = list(set(sortedList))
    sortedList.sort(reverse = False)
    
    for key, value in dic.items():
        dic[key].sort()
    
    for k in sortedList:
        for value in sorted(dic[k]):
            answer.append(value)
        
    return answer