c = int(input())
stk = []

def pop():
    if not stk:
        return -1
    return stk.pop()

def size():
    return len(stk)

def empty():
    if not stk:
        return 1
    else:
        return 0

def top():
    if not stk:
        return -1
    return stk[-1]

for i in range(c):
    x = input()
    if "push" in x:
        x = list(x.split())
        stk.append(x[1])
    elif "pop" in x:
        print(pop())
    elif "size" in x:
        print(size())
    elif "empty" in x:
        print(empty())
    elif "top" in x:
        print(top())
