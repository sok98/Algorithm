# [bronze-1] 1110 더하기 사이클
# algorithm 수학, 구현
# 메모리:   29200 KB
# 시간:     72 ms

firstNum = int(input())
count = 0

num = firstNum
while(count == 0 or int(num)!=firstNum):
    numList = list(map(int, str(num)))
    if len(numList)<2:
        numList.insert(0, 0)
    num = str(numList[1])+str(sum(numList))[-1]
    count+=1

print(count)
