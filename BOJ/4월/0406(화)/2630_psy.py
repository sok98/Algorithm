import sys
input = sys.stdin.readline

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]

white, blue = 0, 0


def divide(x, y, n):
    global white, blue
    color = paper[x][y]
    check = True

    for i in range(x, x+n):
        if not check:
            break

        for j in range(y, y+n):
            if color != paper[i][j]:
                check = False
                divide(x, y, n//2)  # 1사분면
                divide(x, y+n//2, n//2)  # 2사분면
                divide(x+n//2, y, n//2)  # 3사분면
                divide(x+n//2, y+n//2, n//2)  # 4사분면
                break
    if check:
        if color:
            blue += 1
        else:
            white += 1


divide(0, 0, n)
print(white)
print(blue)