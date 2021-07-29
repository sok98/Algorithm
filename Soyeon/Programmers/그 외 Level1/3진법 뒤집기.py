def solution(n):
    answer = 0
    nList = []
    num = n
    
    # 3진법으로 변환
    while num>0:
        nList.insert(0, num%3)
        num //= 3
    
    for i in range(len(nList)):
        print("i", 3**i)
        answer+=nList[i]*(3**i)
    
    return answer