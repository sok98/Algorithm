import sys
input = sys.stdin.readline

N = int(input())

result = [int(input()) for _ in range(3)]
result.sort(reverse=True)

for num in result:
    print(num, end=' ') # 한줄에 띄어쓰기 기준 출력