# [Weekly Chanllenge] 상호 평가
# 획득 포인트 8

def grades(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 50:
        return 'D'
    else:
        return 'F'


def solution(scores):
    answer = ''
    selfScore = []
    newScores = [[] for _ in range(len(scores))]
    

    for n in range(len(scores)):
        for m in range(len(scores)):
            if m==n:
                selfScore.append(scores[n][m])
            else:
                newScores[m].append(scores[n][m])

    for i in range(len(newScores)):
        count = len(scores)
        totalScore = sum(newScores[i])+ selfScore[i]

        # 유일한 최고점 혹은 최저점
        if selfScore[i] not in newScores[i] and (selfScore[i]> max(newScores[i]) or selfScore[i] < min(newScores[i])):
            count-=1
            totalScore -= selfScore[i]

        answer+=grades(totalScore/count)
    

    print(answer)
    return answer


solution([[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]) # "FBABD"
solution([[50,90],[50,87]]) # "DA"
solution([[70,49,90],[68,50,38],[73,31,100]]) # "CFD"