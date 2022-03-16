# !! 헌터, dfs로 모든 경우의 수 구하기
def dfs(hunt, used, ord):
    global min_time
    if sum(used) == hunt * 2:
        time = 0
        now = [0, 0]
        for i in range(len(ord)):
            time += abs(now[0]-loc[ord[i]][0]) + abs(now[1]-loc[ord[i]][1])
            now[0], now[1] = loc[ord[i]][0], loc[ord[i]][1]
        if min_time > time:
            min_time = time
        return
    for i in range(hunt):
        if not used[i]:
            used[i] = True
            dfs(hunt, used, ord + [i+1])
            used[i] = False
        elif not used[i+hunt]:
            used[i+hunt] = True
            dfs(hunt, used, ord + [-i-1])
            used[i+hunt] = False


    

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]
    hunt = 0
    loc = dict()
    for i in range(N):
        for j in range(N):
            if mat[i][j]:
                loc[mat[i][j]] = (i, j)
        if hunt < max(mat[i]):
            hunt = max(mat[i])
    used = [False] * (hunt * 2)
    min_time = 987654321
    dfs(hunt, used, [])
    print("#%d" %tc, end=" ")
    print(min_time)

