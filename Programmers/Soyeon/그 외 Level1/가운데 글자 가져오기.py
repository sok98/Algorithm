import math

def solution1(s):
    answer = ''
    fNum = float(len(s)-1)
    #print(fNum/2)
    floorIndex = math.floor(fNum/2)
    ceilIndex = math.ceil(fNum/2)
    
    #print("floor", floorIndex)
    #print("ceil", ceilIndex)
    
    answer = s[floorIndex:ceilIndex+1]
    # print(answer)
    return answer

# num/2 => float 반환
# num//2 => int 반환 (버림)

def solution2(s):
    answer = ''
    
    answer = s[(len(s)-1)//2:(len(s)+2)//2]
    # print(answer)
    return answer

solution2("abcde") # c
solution2("qwer") # we