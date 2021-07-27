from collections import defaultdict

def solution(genres, plays):
    answer = []
    countDic = defaultdict(lambda: 0) # 딕셔너리 생성 후 value를 0으로 자동 초기화
    genresDic=  defaultdict(lambda: []) # 딕셔너리 생성 후 value를 list로 자동 초기화

    for i in range(len(genres)):
        countDic[genres[i]] += plays[i]
        genresDic[genres[i]].append((plays[i], i)) # (재생 횟수, 인덱스)
  
    countDic = sorted(countDic.items(), key = lambda item: item[1], reverse = True) # 재생 횟수 합 기준 내림차순 정렬

    for i in genresDic:
        genresDic[i] = sorted(genresDic[i], key=lambda x:x[0], reverse=True)[:2]# 장르 내 재생횟수 기준으로 인덱스 내림차순 후 2개만 선택
    
    while len(countDic) > 0:
        genreMax = countDic.pop(0)  # 재생수가 가장 많은 장르
        for i in genresDic:
            if i == genreMax[0]:
                if len(genresDic[i])>1: # 해당 장르의 노래가 2곡 이상이라면
                    answer.append(genresDic[i][0][1])
                    answer.append(genresDic[i][1][1])
                else:
                    answer.append(genresDic[i][0][1])

    print(answer)

    return answer


solution(["classic", "pop", "classic", "classic", "pop", "classic"], [500, 600, 150, 800, 2500, 150]) # [4, 1, 3, 0] # [2500, 600, 800, 500]
solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 500, 2500]) # [4, 1, 0, 3] # [2500, 600, 500, 500]
solution(["classic", "classic", "classic", "pop"], [500, 150, 500, 2500]) # [3, 0, 2] # [2500, 500, 500]
solution(["classic", "jazz", "rock", "pop"], [500, 150, 400, 2500]) # [3, 0, 2, 1] # [2500, 500]
solution(["classic", "pop", "classic", "classic","jazz","pop", "Rock", "jazz"],[500, 600, 150, 800, 1100, 2500, 100, 1000]) # [5, 1, 4, 7, 3, 0, 6]
solution(["classic", "classic", "pop", "classic", "pop", "pop", "classic", "classic", "classic", "classic"], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) # [0, 1, 2, 4]
