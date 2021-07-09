import sys
input = sys.stdin.readline

N, K = map(int, input().split())

list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))

list1.sort()
list2.sort(reverse=True)

for i in range(K):
    list1[i], list2[i] = list2[i], list1[i]

print(sum(list1))