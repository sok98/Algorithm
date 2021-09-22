import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

result = []
queue = deque([])

for i in range(N):
    order = []
    order = list(input().split())

    if order[0] == "push":
        queue.append(order[1])
        # result.append(order[1])
    elif order[0] == "pop":
        if len(queue)==0:
            result.append(-1)
        else:
            result.append(queue.popleft())
    elif order[0] == "size":
        result.append(len(queue))
    elif order[0] == "empty":
        if len(queue)>0:
            result.append(0)
        else:
            result.append(1)
    elif order[0] == "front":
        if len(queue)==0:
            result.append(-1)
        else:
            result.append(queue[0])
    elif order[0] == "back":
        if len(queue)==0:
            result.append(-1)
        else:
            result.append(queue[-1])
    else:
        continue

for r in result:
    print(r)
    