def solution(s, n):
    sList = list(s)
    lower = list("abcdefghijklmnopqrstuvwxyz")
    upper = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    answer = ""
    
    # 아스키코드 n씩 밀기
    for i in range(len(sList)):
        if sList[i] in lower:
            answer += lower[(lower.index(sList[i])+n)%len(lower)]
        elif sList[i] in upper:
            answer += upper[(upper.index(sList[i])+n)%len(upper)]
        else:
            answer+=sList[i]
    return ''.join(answer)

# list.index('A')
# str.find('A')

# 문자 -> 아스키코드 : chr()
# 아스키코드 -> 문자 : ord()