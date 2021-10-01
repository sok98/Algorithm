import sys
input = sys.stdin.readline

array = input().split()
print(array)
input_data = input().split()
n = input_data[0]
target = input_data[1]

def sequential_search(n, target, array):
    # 각 원소를 하나씩 확인
    for i in range(n):
        # 현재의 원소가 찾고자 하는 원소와 동일한 경우
        if array[i] == target:
            # 현재의 위치 반환 (인덱스는 0부터 시작하므로 1 더함)
            return i+1

print(sequential_search(len(array), target, array))
