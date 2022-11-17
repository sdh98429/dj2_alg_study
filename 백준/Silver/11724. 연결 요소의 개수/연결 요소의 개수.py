import sys
from collections import deque


def bfs(u):
  global visited
  q = deque()
  q.append(u)
  flag = 0
  
  while q:
    v = q.popleft()
    if not visited[v]:
      visited[v] = 1
      flag = 1
      for w in range(N+1):
        if adj[v][w] and not visited[w]:
          q.append(w)
  return flag


input = sys.stdin.readline

N, M = map(int, input().split())

adj = [[0]*(N+1) for _ in range(N+1)]
visited = [0] * (N+1)
for _ in range(M):
  u, v = map(int, input().split())
  adj[u][v] = 1
  adj[v][u] = 1
tot = 0
for i in range(1, N+1):
  tot += bfs(i)
print(tot)