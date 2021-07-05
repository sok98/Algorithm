def solution(n):
    answer = []
    nList = list(str(n))
    while(nList):
        answer.append(int(nList.pop(-1)))
    return answer