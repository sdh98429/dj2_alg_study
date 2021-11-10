# Dijkstra ! 특정 거리의 도시 찾기
# Dijkstra는 시간 초과가 나고, bfs로 해결해야 한다.

# Dijkstra로 풀이 (시간 초과)
# import sys
# input = sys.stdin.readline
#
# def Dijkstra(s):
#     U = [0] * (N+1)
#     U[s] = 1
#     D[s] = 0
#
#     for v in d_li[s]:
#         D[v] = 1
#
#     while sum(U) != N:
#         min_w = 987654321
#         for i in range(N+1):
#             if min_w > D[i] and not U[i]:
#                 min_w = D[i]
#                 w = i
#         U[w] = 1
#
#         for v in range(N+1):
#             if v in d_li[w]:
#                 D[v] = min(D[v], D[w]+1)
#
# N, M, K, X = map(int, input().split())
# d_li = [[] for _ in range(N+1)]
# for _ in range(M):
#     A, B = map(int, input().split())
#     d_li[A].append(B)
#
# D = [987654321] * (N+1)
# Dijkstra(X)
#
# flag = 1
# for i in range(len(D)):
#     if D[i] == K:
#         print(i)
#         flag = 0
# if flag:
#     print(-1)


# bfs로 풀이
import sys
input = sys.stdin.readline
from collections import deque

def bfs(s):
    global D
    visited[s] = 1
    q = deque()
    q.append(s)
    while q:
        v = q.popleft()
        for w in d_li[v]:
            if not visited[w]:
                visited[w] = 1
                D[w] = D[v] + 1
                q.append(w)


N, M, K, X = map(int, input().split())
d_li = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    d_li[A].append(B)

D = [0] * (N+1)
visited = [0] * (N+1)
bfs(X)

flag = 1
for i in range(len(D)):
    if D[i] == K:
        print(i)
        flag = 0
if flag:
    print(-1)