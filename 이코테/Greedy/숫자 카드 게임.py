import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(N)]

def solution(N, M, arr):
    answer = 0
    dic = {}
    
    for n in range(N):
        dic[n] = min(arr[n])

    print(max(dic.values()))

solution(N, M, arr)

# solution(3, 3, [[3, 1, 2], [4, 1, 4], [2, 2, 2]])
# solution(2, 4, [[7, 3, 1, 8], [3, 3, 3, 4]]) # 3