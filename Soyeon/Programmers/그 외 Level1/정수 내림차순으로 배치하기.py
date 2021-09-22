def solution(n):
    nList = list(map(int, str(n)))
    nList.sort(reverse=True)
    
    return int(''.join(map(str,nList)))