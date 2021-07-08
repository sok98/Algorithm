# 퀵 정렬(Hoare Partition) 
# 평균: O(N log N)
# 최악의 경우(이미 데이터가 정렬되어 있는 경우): O(N^2)
# 삽입정렬과 시간복잡도 측면에서 반대

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quickSort(array):
    # 리스트가 하나 이하의 원소마을 담고 있다면 종료
    if len(array) <= 1:
        return array
    
    pivot = array[0] # pivot을 담은 첫번째 원소
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트를 반환
    return quickSort(left_side) + [pivot] + quickSort(right_side)

print(quickSort(array))
