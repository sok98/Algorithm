from collections import deque
import sys
input = sys.stdin.readline

N, K = input().rstrip().split()
N = int(N)
K = int(K)
people = deque([])
for i in range(1, N + 1):
    people.append(i)

answer = []
while people:
    people.rotate(-K)
    n = people.pop()
    answer.append(n)

# print(answer)
print("<", end='')
for i in answer[:-1]:
    print(i, end=", ")
print(answer[-1], end=">")
