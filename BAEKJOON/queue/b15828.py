import sys
input = sys.stdin.readline
from collections import deque

q = deque()

N = int(input())

while True:
    n = int(input())
    if n == -1:
        break
    if n:
        if not len(q) == N:
            q.append(n)
    else:
        q.popleft()


if not q:
    print('empty')
else:
    for s in q:
        print(s, end=' ')