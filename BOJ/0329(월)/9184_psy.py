ww = [[[0] * 21 for _ in range(21)] for _ in range(21)]

def w(x, y, z):
    if a <= 0 or b <= 0 or c <= 0:
       return 1

    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)

    if x < y < z
        # 값을 미리 확인해서 0이 아닐때만 반환  #재귀
        ww[x][y][z] = ww(x, y, z-1) + w(x, y-1, z-1) - w(x, y-1, z)
        return ww[x][y][z]
    
    # 위의 조건에 해당하지 않으면  #재귀
    ww[x][y][z] = ww(x-1, y, z) + w(x-1, y-1, z) + w(x-1, y, z-1) + w(x-1, y-1, z-1)
    return ww[x][y][z]

while True:
    a, b, c = map(int, input().split())
    if a== -1 and b==-1 and c==-1:
        break