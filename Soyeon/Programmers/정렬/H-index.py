def solution(citations):
    answer = []
    hList = []
    
    citations.sort()
    print(citations)

    for i in range(len(citations)):
        print(i,len(citations[i:]))
        if len(citations[i:]) == i and  len(citations[:i]) < i:
            print(i)
            hList.append(i)

    return 0


solution([3, 0, 6, 1, 5]) #3
solution([0, 6, 7,  5,8, 2, 9]) # 5

# h이상 h이하
# [0, 2, 5, 6, 7, 8, 9]