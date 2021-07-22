def solution(num):
    num = list(map(str, num))
    print(num)
    # lamda의 x가 key
    # x*3배한 값을 value라 할 때 value로 sort
    # 오름차순 기준 string은 길이가 긴게 뒤에 위치
    num.sort(key = lambda x : x*3, reverse = True)
    print(num)

    return str(int(''.join(num)))

    
solution([6, 10, 2]) #	"6210"
solution([3, 30, 34, 5, 9]) # "9534330"

# permutations 사용하면 시간 초과
# from itertools import permutations

# def solution(numbers):
#     permute = list(permutations(numbers,len(numbers))) 
#     list_permute = [''.join(map(str,i)) for i in permute]
    
#     answer = max(list_permute) 
#     return answer