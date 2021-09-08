  
def solution(people, limit):
    people.sort()
    i, j, answer = 0, len(people) - 1, 0
    while i <= j :
        if people[j] < limit:
            if people[j] + people[i] <= limit:
                i += 1
                
        answer += 1
        j -= 1
        
    return answer