import sys
input = sys.stdin.readline

N = int(input())
count= 0

while N>0:
	if N>=3:
		N-=3
	else:
		N-=1
	count +=1

if count%2==1:
	print('SK')
else:
	print('CY')
