import sys
from typing import Sized
input = sys.stdin.readline

def solution(genres, plays):
    # 중첩 딕셔너리
    answer = []
    # genresDic = {"classic": {1: [0, 1, 3]},  "pop": {1: [2, 4]}}
    genresDic = {} # +indexDic = {}
    countDic = {}

    for i in range(len(genres)):
        if genres[i] not in genresDic:
            genresDic[genres[i]] = {}
            countDic[genres[i]] = 0
        if plays[i] not in genresDic[genres[i]]: # 해당 장르의 곡의 청취 수가 없었으면
            genresDic[genres[i]][plays[i]] = []
        genresDic[genres[i]][plays[i]].append(i)
        countDic[genres[i]] += plays[i]

    
    # print("before", genresDic)


    for value1 in genresDic.values(): # 딕셔너리
        for value2 in value1.values(): # 리스트
            value2 = sorted(value2)

    print("after ", genresDic)
        
    countList = sorted(countDic.items(), key = lambda item: item[1], reverse = True)
    # print(countDic.sort())
    print(len(genresDic['classic']))
    #print(genresDic['classic'])
    #tempList = countList['classic']
    # print(type(countList['classic']))
    
    #print("value size", len(tempList))

    #print(genresDic['A'][0])

    #genresDic = {'classic': {500: [0], 150: [2], 800:[3]}, 'pop': {600: [1], 2500: [4]}}
    #genresDic = {'classic': {1: [0, 1, 3, 6, 7, 8, 9]}, 'pop': {1: [2, 4, 5]}}
    index, listIdx = 0, 0
    for key1, value1 in genresDic.items():
        count = 0
        for key2, value2 in genresDic[key1].items():
            if count >=2:
                break
            listIdx = 0
            print("print", genresDic[countList[index][0]][key2])
            if len(genresDic[countList[index][0]][key2]) <2:
                    answer.append(genresDic[countList[index][0]][key2][0])
                    continue
            else:
                while (count<=2):
                    answer.append(genresDic[countList[index][0]][key2][listIdx])
                    listIdx +=1
                    count+=1

               
                #answer.append(genresDic[countList[index][0]][key2][1])
                #print("test",genresDic[countList[index][0]][key2][0])
                #answer.append(genresDic[countList[index][0]][0][value2][0])
            # 청취 수가 모두 동일하여 하나
            # if len(genresDic[countList[index][0]])<2:
            #     if len(genresDic[countList[index][0]][key2]) <2:
            #         answer.append(genresDic[countList[index][0]][key2][0])
            #         continue
            #     else:
            #         answer.append(genresDic[countList[index][0]][key2][0])
            #         answer.append(genresDic[countList[index][0]][key2][1])
            #     #print("test",genresDic[countList[index][0]][key2][0])
            #     #answer.append(genresDic[countList[index][0]][0][value2][0])
            #     continue
            # # 청취 수가 여러개
            # else:
            #     # 한 청취수에 인덱스가 한개
            #     if len(genresDic[countList[index][0]][key2]) <2:
            #         answer.append(genresDic[countList[index][0]][key2][0])
            #         continue
                    
            #     # 한 청취수에 인덱스가 여러개
            #     else:
            #         answer.append(genresDic[countList[index][0]][key2][0])
            #         answer.append(genresDic[countList[index][0]][key2][1])
            #     # for j in range(2):
            #     #     answer.append(genresDic[countList[index][0]][key2][j])
        index+=1

    
    print(answer)

    return answer

solution(["classic", "pop", "classic", "classic", "pop", "classic"], [500, 600, 150, 800, 2500, 150]) # [4, 1, 3, 0] # [2500, 600, 800, 500]
# solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 500, 2500]) # [4, 1, 0, 3] # [2500, 600, 500, 500]
# solution(["classic", "classic", "classic", "pop"], [500, 150, 500, 2500]) # [3, 0, 2] # [2500, 500, 500]
# solution(["classic", "jazz", "rock", "pop"], [500, 150, 400, 2500]) # [3, 0] # [2500, 500]
# solution(["classic", "pop", "classic", "classic","jazz","pop", "Rock", "jazz"],[500, 600, 150, 800, 1100, 2500, 100, 1000]) # [5, 1, 4, 7, 3, 0, 6]
# solution(["classic", "classic", "pop", "classic", "pop", "pop", "classic", "classic", "classic", "classic"], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) # [0, 1, 2, 4]
