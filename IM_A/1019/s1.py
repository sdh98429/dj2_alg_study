T = int(input())

def DFS(vr, vc, lev):
    global eat
    board[vr][vc] = 0
    if lev == 3:
        return
    for m in range(4):
        flag = 0
        for dist in range(1, N):
            wr = vr + dr[m] * dist
            wc = vc + dc[m] * dist
            if wr in range(N) and wc in range(N):
                if flag:
                    if board[wr][wc] == 0:
                        DFS(wr, wc, lev+1)
                    else:
                        board[wr][wc] = 0
                        eat.add((wr, wc))
                        DFS(wr, wc, lev+1)
                        board[wr][wc] = 1
                        break

                if not flag and board[wr][wc] == 1:
                    flag = 1


dr = (0, 0, 1, -1)
dc = (1, -1, 0, 0)

for tc in range(1, T+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if board[i][j] == 2:
                si, sj = i, j
    eat = set()
    DFS(si, sj, 0)
    print('#{} {}'.format(tc, len(eat)))