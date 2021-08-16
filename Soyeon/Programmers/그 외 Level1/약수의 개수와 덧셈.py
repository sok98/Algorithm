def solution(left, right):
    answer = 0
    
    for i in range(left, right+1):
        count=0
        cList = []
        
        for k in range(1, i+1):
            if i%k==0:
                cList.append(k)
                count+=1
                
        if count%2==0:
            answer+=i
        else:
            answer-=i
    
    return answer

def bestSolution(left, right):
    answer = 0
    
    for i in range(left, right+1):
        if int(i**0.5)==(i**0.5):
            answer-=i
        else:
            answer+=i
    
    return answer
