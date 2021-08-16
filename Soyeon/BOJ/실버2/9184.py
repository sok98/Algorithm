import sys
input = sys.stdin.readline

result = []
wDic = {}

def w(a, b, c):
    if (a, b, c) in wDic:
        return wDic[(a, b, c)]
    else:
        if a <= 0 or b <= 0 or c <= 0:
            wDic[(a, b, c)] = 1
            return wDic[(a, b, c)]

        if a > 20 or b > 20 or c > 20:
            wDic[(a,b,c)] = w(20, 20, 20)
            return w(20, 20, 20)

        if a < b and b < c:
            wDic[(a, b, c)] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
            return w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)

        else:
            wDic[(a, b, c)] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
            return w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)

while(True):
    a, b, c = map(int, input().split())

    if a==-1 and b==-1 and c==-1:
        break
    else:
        result.append(f"w({a}, {b}, {c}) = {w(a,b,c)}")

for r in result:
    print(r)
