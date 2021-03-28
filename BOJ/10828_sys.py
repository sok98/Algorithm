N = int(input())
stack = []


def pop():
    if not stack:
        return -1
    return stack.pop()


def size():
    return len(stack)


def empty():
    if not stack:
        return 1
    else:
        return 0


def top():
    if not stack:
        return -1
    return stack[-1]


for i in range(N):
    cmd = input()

    # 정수를 스택에 넣는 연산
    if "push" in cmd:
        x = list(cmd.split())
        stack.append(x[1])

    elif "pop" in cmd:
        print(pop())
    elif "size" in cmd:
        print(size())
    elif "empty" in cmd:
        print(empty())
    elif "top" in cmd:
        print(top())
