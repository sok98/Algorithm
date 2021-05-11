# [silver-2] 1541 잃어버린 괄호
# algorithm 브루트포스
# 메모리: 28776KB
# 시간: 68ms

import sys
input = sys.stdin.readline

sList = input().split('-')
sum = 0

for i in sList[0].split('+'):
    sum+=int(i)

for i in sList[1:]:
    for j in i.split('+'):
        sum-=int(j)

print(sum)


# Fail Case

# formula=str(input())
# numList = []

# # - 기호가 없으면
# if formula.find('-')<0:
#     print(formula)
#     print(eval(formula))

# # - 기호가 1개 이상
# else:
#     # eval() 사용 시 Syntax Error 방지
#     formula=formula.replace('-0', '-') 
#     formula=formula.replace('+0', '-')

#     formula=formula.replace('-', ')-(')
#     formula = formula[:formula.find(')')]+formula[formula.find('-'):]
#     numList = list(formula)
#     numList.insert(len(formula)-1,')')

#     # eval() 사용 시 Syntax Error 방지
#     while numList[0]=='0':
#         numList.pop(0)
#     formula = ''.join(numList)
#     print(eval(formula))
