# dfs 현수막
# bfs 해결
from collections import deque

def bfs(i, j):
    visited[i][j] = 1
    q = deque()
    q.append((i, j))
    while q:
        wr, wc = q.popleft()
        for m in range(8):
            vr = wr + dr[m]
            vc = wc + dc[m]
            if vr in range(M) and vc in range(N) and screen[vr][vc] and not visited[vr][vc]:
                visited[vr][vc] = 1
                q.append((vr, vc))


dr = [0, 0, 1, -1, 1, 1, -1, -1]
dc = [1, -1, 0, 0, 1, -1, 1, -1]

M, N = map(int, input().split())
visited = [[0] * N for _ in range(M)]
screen = []
for _ in range(M):
    screen.append(list(map(int ,input().split())))

ans = 0
for i in range(M):
    for j in range(N):
        if screen[i][j] and not visited[i][j]:
            ans += 1
            bfs(i, j)

print(ans)