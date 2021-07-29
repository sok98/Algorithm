def solution(s):
    answer = True
    pCount = 0
    yCount=0
    sList = list(s)
    
    for i in s:
        if i == 'p' or i == 'P':
            pCount+=1
        elif i == 'y' or i == 'Y':
            yCount+=1
    
    if pCount==yCount:
        return True
    else:
        return False

    return True