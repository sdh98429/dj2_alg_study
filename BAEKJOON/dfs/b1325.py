# dfs 효율적인 해킹
# pypy3 써야함

import sys
from collections import deque

input = sys.stdin.readline

def bfs(start):
    q = deque()
    cnt = 0
    q.append(start)
    visited[start] = 1
    while q:
        v = q.popleft()
        for w in d_list[v]:
            if not visited[w]:
                visited[w] = 1
                q.append(w)
                cnt += 1
    return cnt

N, M = map(int, input().split())

hack = [0] * (N+1)
d_list =[[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    d_list[B].append(A)
max_cnt = 0
ans = []
for s in range(1, N+1):
    visited = [0] * (N+1)
    now_cnt = bfs(s)
    if now_cnt > max_cnt:
        ans = []
        max_cnt = now_cnt
        ans.append(s)
    elif now_cnt == max_cnt:
        ans.append(s)
print(*ans)
