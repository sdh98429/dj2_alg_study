from collections import deque

def bfs(i, j):
    global mat
    cnt = 1
    q = deque()
    q.append((i, j, cnt))
    while q:
        vr, vc, cn = q.popleft()


        if vr == N-1 and vc == M-1:
            return cn

        if mat[vr][vc]:
            mat[vr][vc] = 0
            for d in range(4):
                wr = vr + dr[d]
                wc = vc + dc[d]
                if wr in range(N) and wc in range(M):
                    q.append((wr, wc, cn+1))



N, M = map(int, input().split())
mat = [list(map(int, list(input()))) for _ in range(N)]

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

print(bfs(0, 0))