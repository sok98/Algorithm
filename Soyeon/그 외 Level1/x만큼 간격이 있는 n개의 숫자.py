def solution(x, n):
    answer = []
    # x = int(x)
    # n = int(n)
    
    for i in range(n):
        answer.append(x*(i+1))
    
    print(answer)
    return answer

solution(2,	5) # [2,4,6,8,10]
solution(4, 3)	# [4,8,12]
solution(-4, 2)	# [-4, -8]