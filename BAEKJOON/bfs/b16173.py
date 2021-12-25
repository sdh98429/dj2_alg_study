# bfs 점프왕 쩰리 (Small)
# 뉴로클 2번 문제와 같음
from collections import deque

def bfs(i, j):
    q = deque()
    visited[i][j] = 1
    q.append((i, j))
    while q:
        wr, wc = q.popleft()
        if wr == N-1 and wc == N-1:
            return 'HaruHaru'

        for m in range(2):
            vr = wr + dr[m]*M[wr][wc]
            vc = wc + dc[m]*M[wr][wc]
            if vr in range(N) and vc in range(N) and not visited[vr][vc]:
                visited[vr][vc] = 1
                q.append((vr, vc))
    else:
        return 'Hing'

dr = [1, 0]
dc = [0, 1]


N = int(input())
M = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

print(bfs(0, 0))