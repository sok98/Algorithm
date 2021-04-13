import sys
input = sys.stdin.readline

N, M = map(int, input().split())

card = list(map(int, input().split(' ')))
card.sort(reverse=True)

def sumCard(card):
    answer = 0
    for a in range(0, N-2):
        for b in range(a+1, N-1):
            for c in range(b+1, N):
                if (card[a]+card[b]+card[c])<=M and card[a]+card[b]+card[c] > answer:
                    answer = card[a]+card[b]+card[c]
    print(answer)

sumCard(card)