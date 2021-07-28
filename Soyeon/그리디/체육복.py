def solution(n, lost, reserve):
    answer = 0
    tempLost = lost.copy() # python은 복사가 참조 => tempLost = lost하면 원본 배열 또한 영향이 간다
    
    # lost와 reserve의 중복 원소 제거
    for i in lost:
        if i in reserve:
            reserve.remove(i)
            tempLost.remove(i)

    if len(lost)<1:
        return n

    lost = tempLost.copy()
    
    for i in lost:
        # lost[n]-1이 reserve에 있으면 reserve에서 제거 => continue
        if i-1 in reserve:
            reserve.remove(i-1)
            tempLost.remove(i)
        
        # lost[n]+1이 reserve에 있으면 reserve에서 제거 => continue
        elif i+1 in reserve:
            reserve.remove(i+1)
            tempLost.remove(i)
    
    lost = tempLost.copy()

    answer = n - len(lost)
    print(answer)
    
    return answer

#solution(5, [2, 4],	[2, 4, 5]) # 5
#solution(5, [2, 4],	[1, 3, 5]) # 5
#solution(5, [2, 4],	[3]) # 4
solution(3,	[3],    [1]) # 2