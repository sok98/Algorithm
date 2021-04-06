from itertools import permutations

def solution(numbers):
    answer = 0
    # 에라토스테네스의 체 1~10000000 (numbers : 7이하 문자열)
    n = 10000000
    check = [i for i in range(0, n+1)]
    check[1] = 0
    i = 2
    while i*i <= n:
        for j in range(i*i, n+1, i):
            check[j] = 0 # 소수가 아닌 것들은 0
        i += 1
    # numbers - permutations 순열 적용
    nset = set()
    nlist = []
    for i in range(1, len(numbers)+1):
        nlist = list(map(''.join, permutations(numbers, i))) # map 활용 익히기
        for nl in nlist:
            nset.add(int(nl))
    for num in nset:
        if check[num] != 0:
            answer += 1
    return answer



# 시간초과 코드 
# prime = []
# n = 10000000
# check = [False, False] + [True] * n
# i = 2
# while i*i <= n: # 시간초과 -> sqrt(n)까지만 확인하도록
#         if check[i] == True:
#             prime.append(i)
#         for j in range(i*i, n+1, i): 
#             check[j] = False
#         i += 1
