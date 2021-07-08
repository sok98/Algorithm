import sys
input = sys.stdin.readline

# N = int(input())

def solution(N):
    primeNum = []

    for num in range(2, N+1):
        count = 0

        for i in range(1, num+1):
            if count>2:
                break
            elif num%i==0:
                count+=1
        
        if count==2:
            primeNum.append(num)
    print(len(primeNum))
    return len(primeNum)

solution(10) # 4 [2, 3, 5, 7]
# solution(5) # 3 [2, 3, 5]