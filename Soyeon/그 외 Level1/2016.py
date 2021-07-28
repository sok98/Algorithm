def solution(a, b):
    answer = ''
    daySum = 0
    days = ['THU','FRI','SAT','SUN','MON','TUE','WED']
    dow = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    
    for key, value in dow.items():
        if key < a:
            print("sum month: ", key, "days: ", value)
            daySum +=value
    print(daySum)
    #print((daySum+b)%7)
    answer = days[(daySum+b)%7]
    print(answer)
    
    return answer

solution(1, 1) # FRI
solution(5, 24) # TUE