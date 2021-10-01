import sys
input = sys.stdin.readline

N = int(input())
student = []

for _ in range(N):
    name, score = input().split()
    student.append((name, int(score)))

# student의 점수를 기준으로 sort
student.sort(key=lambda list: list[1])

for person in student:
    print(person[0], end=' ')