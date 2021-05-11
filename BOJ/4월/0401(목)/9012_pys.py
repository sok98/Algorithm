import sys
lines = int(sys.stdin.readline())
commands = []
for _ in range(lines):
    commands.append(sys.stdin.readline())

for command in commands:
    stack = []
    for c in command:
        # 스택에 비어있다면 일단 삽입
        if len(stack) == 0: 
            stack.append(c)
        # 스택 가장 상단이 '(', 입력 받은게 ')'라면 스택에서 '(' 제거
        elif stack[-1] == '(' and c == ')':
            stack.pop()
        # 그 외엔 일단 삽입
        else: stack.append(c)

    # 스택에 남은게 없다면 VFS
    if stack: print("NO")
    else: print("YES")

    #TODO: dic로 풀어보기