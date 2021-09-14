#[2018 카카오 블라인드] 비밀지도
# 획득 포인트 1
# O(N**2)

def solution(n, arr1, arr2):
    answer = []
    bitMul = []
    
    for i in range(n):
        bitMul.append(arr1[i] | arr2[i]) # 비트 연산 결과를 10진수로 저장
    
    for i in list(map(bin,bitMul)) :
        i = i[2:]
        if len(i) < n : # 부족한 자리수 0으로 채움
            i = '0'*(n-len(i)) + i 
        trans = i.replace('1','#').replace('0',' ')
        answer.append(trans)
    
    return answer


# 다른 코드
# def solution(n, arr1, arr2):
#     answer = []
#     for decimal1, decimal2 in zip(arr1, arr2):
#         binary12 = str(bin(decimal1 | decimal2))[2:]
#         binary12 = '0' * (n - len(binary12)) + binary12
#         binary12 = binary12.replace('1', '#')
#         binary12 = binary12.replace('0', ' ')
#         answer.append(binary12)
# return answer