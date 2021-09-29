from collections import deque
N, K = map(int, input().split())

num = input()

stack = deque([int(num[0])])
for i in range(1, N):
    if not K:
        break
    p = stack.pop()
    while p < int(num[i]) and K:
        K -= 1
        if not stack:
            break
        p = stack.pop()
    else:
        stack.append(p)
        stack.append(int(num[i]))
        continue
    stack.append(int(num[i]))
else:
    i += 1

if not K:
    while stack:
        print(stack.popleft(), end='')
    print(num[i:])
else:
    for _ in range(len(stack)-K):
        print(stack.popleft(), end='')

# 5 2
# 81765

# 4 1
# 4321