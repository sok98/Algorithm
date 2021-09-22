def solution(n):
    answer = []
    pattern = ['수', '박']
    
    for i in range(n):
        answer.append(pattern[i%len(pattern)])
    
    return ''.join(answer)