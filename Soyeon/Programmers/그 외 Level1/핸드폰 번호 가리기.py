def solution(phone_number):
    answer = ''
    
    for i in range(len(phone_number)-4):
        answer +='*'
    answer +=phone_number[len(phone_number)-4:]
    print(answer)
    return answer

solution("01033334444") # "*******4444"
solution("027778888") # "*****8888"
