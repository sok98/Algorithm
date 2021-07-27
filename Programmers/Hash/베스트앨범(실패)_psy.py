import sys
from typing import Sized
input = sys.stdin.readline

def solution(genres, plays):
    answer = []
    genresDic = {}
    countDic = {}
    indexDic = {}

    for i in range(len(genres)):
        if plays[i] not in indexDic:
            indexDic[plays[i]] = []
        indexDic[plays[i]].append(i)

        if genres[i] not in genresDic:
            genresDic[genres[i]] = []
            countDic[genres[i]] = 0
        countDic[genres[i]] += plays[i]
        genresDic[genres[i]].append(plays[i])

    
    #print("before", genresDic)

    for value in genresDic.values():
        value.sort(reverse = True)
    for value in indexDic.values():
        value.sort()

    #print("after", genresDic)
        
    countList = sorted(countDic.items(), key = lambda item: item[1], reverse = True)
    # print(countDic.sort())
    # print(countList)

    for i in range(2):
        if len(genresDic[countList[i][0]])<2:
            answer.append(indexDic[genresDic[countList[i][0]][0]][0])
            continue
        else:
            idx = 0
            for j in range(2):
                if len(indexDic[genresDic[countList[i][0]][j]])>1:
                    answer.append(indexDic[genresDic[countList[i][0]][j]][idx])
                    idx+=1
                else:
                    answer.append(indexDic[genresDic[countList[i][0]][j]][0])
    
    # print(answer)

    return answer

## solution(["classic", "pop", "classic", "classic", "pop", "classic"], [500, 600, 150, 800, 2500, 150]) # [4, 1, 3, 0] # [2500, 600, 800, 500]
# solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 500, 2500]) # [4, 1, 0, 3] # [2500, 600, 500, 500]
# solution(["classic", "classic", "classic", "pop"], [500, 150, 500, 2500]) # [3, 0, 2] # [2500, 500, 500]
# solution(["classic", "jazz", "rock", "pop"], [500, 150, 400, 2500]) # [3, 0] # [2500, 500]
# solution(["classic", "pop", "classic", "classic","jazz","pop", "Rock", "jazz"],[500, 600, 150, 800, 1100, 2500, 100, 1000]) # [5, 1, 4, 7, 3, 0, 6]
solution(["classic", "classic", "pop", "classic", "pop", "pop", "classic", "classic", "classic", "classic"], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) # [0, 1, 2, 4]
