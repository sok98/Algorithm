# [silver-5] 1427 소트인사이드
# algorithm 정렬
# 메모리: 	29200 KB
# 시간:     80 ms

N = list(map(int, input()))

print(int(''.join([str(int) for int in sorted(N, reverse=True)])))
