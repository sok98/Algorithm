def solution(arr):
    answer = []
    
    preNum = arr[0]
    answer.append(arr[0])
    
    for i in arr:
        if i != preNum:
            answer.append(i)
            preNum = i
    
    return answer