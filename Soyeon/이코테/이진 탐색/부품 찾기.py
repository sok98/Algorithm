import sys
input = sys.stdin.readline

# O(N)
def binary_search(target, array, start, end):
    while start<=end:
        mid = (start+end)//2

        if array[mid]==target:
            return "yes"
        elif array[mid]>target:
            end = mid-1
        elif array[mid]<=target:
            start = mid+1
    return "no"

result = ""
N = int(input())
listN = list(map(int, input().split()))
M = int(input())
listM = list(map(int, input().split()))

for item in listM:
    result+=binary_search(item, listN, 0, len(listN)-1)+" "
print(result.rstrip())
