import sys
c =  int(sys.stdin.readline())
q = []

def pop():
    if not q:
        return -1
    del q[0]
    return q


def size():
    return len(q)

def empty():
    if not q:
        return 1
    else:
        return 0

def front():
    if not q:
        return -1
    return q[0]

def back():
    if not q:
        return -1
    return q[-1]

for i in range(c):
    x = input()
    if "push" in x:
        x = list(x.split())
        q.append(x[1])
    elif "pop" in x:
        print(pop())
    elif "size" in x:
        print(size())
    elif "empty" in x:
        print(empty())
    elif "front" in x:
        print(front())
    elif "back" in x:
        print(front())
