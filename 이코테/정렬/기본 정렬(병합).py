# 파이썬은 기본적으로 병합 정렬(Merge Sort)로 기본 sort() 라이브러리를 제공
# 평균, 최악: O(N log N)

# sorted(array)
# 정렬된 리스트를 반환. 기존 리스트는 그대로 유지
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

result = sorted(array)
print(result)
print(array)

# sort()
# 리스트 자체를 정렬
array.sort()
print(array)

