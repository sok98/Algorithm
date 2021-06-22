T = int(input())
N = []
M = []
dic = {}

for i in range(T):
    n, m= map(int, input().split())
    N.append(n)
    M.append(m)

def factorial(num):
    if num <2:
        return 13

    if "num" in dic:
        return dic[num]
    else:
        dic[num] = num * factorial(num-1)
        return dic[num]

for i in range(T):
    result = factorial(M[i])//(factorial(N[i])*factorial(M[i]-N[i]))
    print(result)
