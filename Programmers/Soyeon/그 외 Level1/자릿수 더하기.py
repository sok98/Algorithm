def solution(n):
    answer = 0
    numList = list(str(n))

    for i in numList:
        answer+=int(i)

    return answer