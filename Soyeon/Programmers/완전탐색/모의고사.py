def solution(answers):
    firstPrice = []
    score = {}
    
    # 3명의 패턴 배열을 저장
    pattern1 = [1, 2, 3, 4, 5]
    pattern2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    # answer의 길이만큼 각 패턴의 아이템을 답안으로 가져옴
    sheet1, sheet2, sheet3 = [], [], []
    
    for i in range(len(answers)): # i=10 이면 
        sheet1.append(pattern1[i%len(pattern1)])
        sheet2.append(pattern2[i%len(pattern2)])
        sheet3.append(pattern3[i%len(pattern3)])

    # print("sheet1", sheet1)
    # print("sheet2", sheet2)
    # print("sheet3", sheet3)
    
    # answers의 각 요소를 기준으로 3명의 답 채점 -> dic에 저장
    for i in range(len(answers)):
        if sheet1[i]==answers[i]:
            if 1 in score:
                score[1]+=1
            else:
                score[1]=1
                
        if sheet2[i]==answers[i]:
            if 2 in score:
                score[2]+=1
            else:
                score[2]=1
                
        if sheet3[i]==answers[i]:
            if 3 in score:
                score[3]+=1
            else:
                score[3]=1
    
    
    # value 중 max의 값과 같은 key를 answer 배열에 추가
    for key, value in score.items():
        if value == max(score.values()):
            firstPrice.append(key)
            
    # 오름차순으로 sort하여 return
    return sorted(firstPrice, reverse=False) #reverse=False는 오름차순

print(solution([1,2,3,4,5])) # [1]
print(solution([1,3,2,4,2])) # [1,2,3]