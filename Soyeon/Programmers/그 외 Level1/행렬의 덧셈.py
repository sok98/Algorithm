def solution(arr1, arr2):
    answer = [[]]
    answer = arr1.copy()

    
    for i in range(len(arr1)):
        for j in range(len(arr1[i])):
            answer[i][j] = arr1[i][j] + arr2[i][j]
    
    print(answer)
    return answer

# solution([[1,2],[2,3]], [[3,4],[5,6]])	# [[4,6],[7,9]]
# solution([[1],[2]], [[3],[4]])	# [[4],[6]]


# 이차원 배열의 초기화 방법
# array = [[0]*11 for i in range(10)]
# array = [[0 for col in range(11)] for row in range(10)]