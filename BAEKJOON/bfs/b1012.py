# bfs 유기농 배추
# 평범한 bfs 문제
T = int(input())

def BFS(i, j):
    global cnt
    if visited[i][j] or not farm[i][j]:
        return
    cnt += 1
    q = []
    visited[i][j] = 1
    q.append((i, j))
    while q:
        vr, vc = q.pop(0)
        for m in range(4):
            wr = vr + dr[m]
            wc = vc + dc[m]
            if wr in range(N) and wc in range(M) and farm[wr][wc] and not visited[wr][wc]:
                visited[wr][wc] = 1
                q.append((wr, wc))


dr = (0, 0, 1, -1)
dc = (1, -1, 0, 0)

for tc in range(1, T+1):
    M, N, K = map(int, input().split())
    farm = [[0] * M for _ in range(N)]
    visited = [[0]* M for _ in range(N)]
    cnt = 0
    for _ in range(K):
        X, Y = map(int, input().split())
        farm[Y][X] = 1
    for i in range(N):
        for j in range(M):
            BFS(i, j)
    print(cnt)