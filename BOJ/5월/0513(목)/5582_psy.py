# [gold-5] 5582 공통 부분 문자열
# algorithm 다이나믹 프로그래밍
# 메모리: KB
# 시간: ms

import sys
input = sys.stdin.readline

N = list(input())
M=list(input())
a = list(N)
b=list(M)

if(len(a)>len(b)): # a가 더 짧은 리스트
    temp = []
    temp = a
    a=b
    b=temp


i, j=0, 0
sList = []
size=0
for i in range(len(a)):
	for j in range(len(b)):
		if a[i]==b[i]:
			k=i
			while a[k]==b[k]:
				k+=1
				size = k-i+1
			sList.append(size)
print(max(sList))


