N, M = map(int, input().split())
person = []
answer = []
dic= {}

for _ in range(N+M):
	person.append(input())

for i in range(N+M):
	if person[i] in dic:
		dic[person[i]] += 1
	else:
		dic[person[i]] = 1

for key, value in dic.items():
    if value ==2:
            answer.append(key)
		
print(len(answer))
answer.sort()
for i in range(len(answer)):
	print(answer[i])
