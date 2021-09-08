import itertools

def solution(numbers):
    # 숫자의 조합 (중복x)
    nList = []
    nums =[]
    primeNum = []

    for i in range(1, len(numbers)+1):
        nList+=list(itertools.permutations(list(numbers), i))

    for item in nList:
        nums.append(int(''.join(item)))
    nums = sorted(list(set(nums)))

    # 오름차순 -> 소수 찾기 (에라토스테네스의 체)
    max = nums[-1]
    primes = [True for i in range(max+1)]

    for i in range(2, int(pow(max, 1/2))+1):
        if primes[i] == True: # i가 소수인 경우(남은 수인 경우)
            # i를 제외한 i의 모든 배수를 지우기
            j=2
            while i*j <= max:
                primes[i*j] = False
                j+=1
    
    # 조합한 수가 소수 list에 있디면
    for num in nums:
        if num>1 and primes[num]:
            primeNum.append(num)

    return len(primeNum)

# print(solution("011")) # 2 # [11, 101] 
# print(solution("17")) # 3 # [7, 17, 71]
