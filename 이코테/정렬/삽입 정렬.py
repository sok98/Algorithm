# 삽입 정렬 # O(N^2)
# 일정 부분 이미 정렬이 되어 있는 경우 유리 => O(N)
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j-1]: # 내림차순: if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break

print(array)