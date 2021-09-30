from collections import deque
import sys
input = sys.stdin.readline

N, P = map(int, input().split())
stack = [deque([]) for _ in range(7)]
tot = 0
for _ in range(N):
    L, M = map(int, input().split())
    while stack[L]:
        p = stack[L].pop()
        if p < M:
            stack[L].append(p)
            stack[L].append(M)
            tot += 1
            break
        elif p > M:
            tot += 1
            continue
        stack[L].append(p)
        break
    else:
        stack[L].append(M)
        tot += 1
print(tot)

