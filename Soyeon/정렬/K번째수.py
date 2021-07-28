def solution(array, commands):
    answer = []
    
    # 배열 슬라이스 -> 정렬 -> i-1번째 수 출력
    for command in commands:
        tempList = []

        tempList = array[command[0]-1:command[1]]

        print("tempList", tempList)

        tempList.sort()

        print("Sorted", tempList, "\n")
        answer.append(tempList[command[2]-1])
    
    print(answer)
    
    return answer


solution([1, 5, 2, 6, 3, 7, 4],	[[2, 5, 3], [4, 4, 1], [1, 7, 3]]) # [5, 6, 3]