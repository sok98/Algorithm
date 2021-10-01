# import sys
# input = sys.stdin.readline

# N, M, K = map(int, input().split())
# numbers = list(map(int, input().split()))

def solution(N, M, K, numbers):

    # numbers를 정렬, 중복 제거
    numbers = list(set(numbers))
    numbers.sort(reverse=True)
    print("numbers", numbers)
    

    # range(M) 동안 number[0]를 sum하고 count++
    count, sum = 0, 0
    for _ in range(M):
        # 만약 count=3이면 number[1]를 sum하고 count=0 
        if count<3:
            sum += numbers[0]
            count+=1
        else:
            sum += numbers[1]
            count=0

    print("sum:", sum)

# solution(5, 8, 3, [2, 4, 5, 4, 6])

def solution2(N, M, K, numbers):
    count, result = 0, 0
    numbers.sort(reverse=True)

    first = numbers[0]
    second = numbers[1]

    # 가장 큰 수가 더해지는 count
        # 6+6+6+5+6+6+6+5+6
        # int ( 9 / 4 ) * 3 => 6
        # 9 % 4 => 1
    count = int(M/(K+1))*K
    count += M % (K+1)

    

    result = count * first
    result += (M-count)*second

    print(result)

# solution2(5, 8, 3, [2, 4, 5, 4, 6])