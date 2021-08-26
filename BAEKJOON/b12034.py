
# 2
# 3
# 15 20 60 75 80 100
# 4
# 9 9 12 12 12 15 16 20
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    P = list(map(int, input().split()))
    stack = []
    result = ''
    while P:
        p = P.pop()
        if stack:
            for i in range(len(stack)):
                if p == int(stack[i] * 3/4):
                    stack.pop(i)
                    result = str(p) + ' ' + result
                    break
            else:
                stack.append(p)
        else:
            stack.append(p)


    print('Case #{}: {}'.format(tc, result))
