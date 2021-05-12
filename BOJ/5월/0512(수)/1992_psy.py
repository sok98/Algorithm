# [silver-1] 1992 쿼드트리
# algorithm 분할정복, 재귀
# 메모리: 28776KB
# 시간: 68ms

import sys
input = sys.stdin.readline

N = int(input())
image = [list(map(int, input().strip())) for _ in range(N)]

def quadtree(x, y, n):
    # 크기 1x1
    if(n==1):
        return str(image[x][y])
    
    result =[]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if(image[i][j] != image[x][y]):
                # extend는 list, tuple, dict 등의 iterable object를
                # list 끝에 append
                result.append('(')
                result.extend(quadtree(x, y, n//2))
                result.extend(quadtree(x, y+n//2, n//2))
                result.extend(quadtree(x+n//2, y, n//2))
                result.extend(quadtree(x+n//2, y+n//2, n//2))
                result.append(')')

                return result
    return str(image[x][y])


print(''.join(quadtree(0, 0, N)))