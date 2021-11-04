# backtracking 컴백홈

def dfs(i, j, k):
    global ans
    if k == K:
        if i == 0 and j == C-1:
            ans += 1
        return

    for m in range(4):
        wr = i + dr[m]
        wc = j + dc[m]
        if wr in range(R) and wc in range(C) and maze[wr][wc] == '.':
            maze[wr][wc] = 'T'
            dfs(wr, wc, k+1)
            maze[wr][wc] = '.'

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

R, C, K = map(int, input().split())

maze = [list(input()) for _ in range(R)]

ans = 0
maze[R-1][0] = 'T'
dfs(R-1, 0, 1)
print(ans)