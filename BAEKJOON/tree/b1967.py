# tree !! 트리의 지름 pypy3
# 메모리 초과 및 시간 초과가 어려웠음
# n*n 리스트는 메모리가 너무 커서 이중리스트에 튜플 형태로 거리를 넣고
# 트리의 지름이 되기 위해서 리프노드를 선별해서 bfs 실행

import sys
input = sys.stdin.readline
from collections import deque

def bfs(s, dist):
    global ans
    q = deque()
    q.append((s, dist))
    visited[s] = 1
    while q:
        v, d = q.popleft()
        leaf = 1
        for w in d_li[v]:
            if not visited[w[0]]:
                visited[w[0]] = 1
                leaf = 0
                q.append((w[0], d+w[1]))
        if leaf:
            if d > ans:
                ans = d


N = int(input())
d_li = [[] for _ in range(N+1)]


for _ in range(N-1):
    a, b, l = map(int, input().split())
    # 이중 리스트에 튜플 형태로 거리까지 넣는다
    d_li[a].append((b, l))
    d_li[b].append((a, l))


ans = 0

for st in range(1, N+1):
    # 리프 노드
    if len(d_li[st]) == 1:

        visited = [0] * (N + 1)
        bfs(st, 0)
print(ans)