# [Weekly Chanllenge] 모음 사전
# 획득 포인트 1

from itertools import product
def solution(word):
    alpha = ['A', 'E', 'I', 'O', 'U']
    words = []

    for i in range(1, len(alpha)+1):
        for j in product(alpha, repeat=i):
            words.append(''.join(j))

    return sorted(words).index(word)+1