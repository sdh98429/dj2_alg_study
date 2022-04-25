# ! 스택, 입력값 길어 sys stdin readline
import sys

# N = int(input())
N = int(sys.stdin.readline().strip())
top = -1
stack = [-1] * (N+1)

# def push(i):
#     global stack, top
#     top += 1
#     stack[top] = int(i)


# def pop():
#     global stack, top
#     if top >= 0:
#         print(stack[top])
#         top -= 1
#     else:
#         print(-1)

for _ in range(N):
    # cmd = input().split()
    cmd = list(sys.stdin.readline().strip().split())
    if cmd[0] == 'push':
        # push(cmd[1])
        top += 1
        stack[top] = int(cmd[1])
    elif cmd[0] == 'pop':
        # pop()
        if top >= 0:
            print(stack[top])
            top -= 1
        else:
            print(-1)
    elif cmd[0] == 'size':
        print(top+1)
    elif cmd[0] == 'empty':
        print(1 if top == -1 else 0)
    elif cmd[0] == 'top':
        print(stack[top])

