def solution(n):
    if(pow(n, 0.5) == int(pow(n, 0.5))):
        return (pow(n, 0.5)+1)**2
    else:
        return -1