# [Weekly Chanllenge] 부족한 금액 계산하기
# 획득 포인트 4

def solution(price, money, count):
    sum = 0
    
    for i in range(1, count+1):
        sum+=(i*price)
    answer = sum - money
    
    if answer < 0:
        answer = 0
    
    return answer