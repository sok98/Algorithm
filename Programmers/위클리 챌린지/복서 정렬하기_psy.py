# [Weekly Chanllenge] 복서 정렬하기
# 획득 포인트 13
    
    # 붙은 적 있는 승률 높은 복서가 앞
    # 승률이 동일 => 무거운 복서를 이긴 횟수가 많을수록 앞
    # 승률도 동일 => 본인 몸무게 무거운 선수가 앞
    # 작은 번호 앞
    
def solution(weights, head2head):
    answer = []
    
    # (승률, 무거운 복서를 이긴 횟수, 본인 몸무게, 작은 번호)
    person = [list([0]*4) for _ in range(len(weights))]
    
    for i in range(len(weights)):
        fight, win = 0, 0
        
        for j in range(len(weights)):
            if head2head[i][j] == 'W':
                fight += 1
                win += 1
                winner, loser = i, j
                # 승리 횟수
                person[winner][0] += 1 
                # 자기보다 무거운 복서를 이긴 횟수
                if  weights[winner] < weights[loser]:
                    person[winner][1] += 1
            elif head2head[i][j] == 'L':
                fight += 1
            else:
                continue
        # 승률
        if fight==0:
            person[i][0] = 0
        else:
            person[i][0] = win/fight*100
        # 본인 몸무게
        person[i][2] = weights[i]
        # 번호
        person[i][3] = i
            
    person = sorted(person, key = lambda x : (-x[0], -x[1], -x[2], x[3]))

    for p in person:
        answer.append(p[3]+1)
            
    return answer

#solution([50,82,75,120],["NLWL","WNLL","LWNW","WWLN"]) #	[3,4,1,2]
#solution([145,92,86],	["NLW","WNL","LWN"]) #	[2,3,1]
#solution([60,70,60],	["NNN","NNN","NNN"]) #	[2,1,3]