# dfs 섬의 개수
# 재귀로 해보려했지만 최대깊이 초과
# bfs 자주 쓰지만 이번엔 dfs로 해결해 봄
def dfs(vr, vc):
    global cnt
    # 방문하지 않은 지역이고 땅이라면 cnt 추가
    if not visited[vr][vc] and world[vr][vc] == 1:
        cnt += 1
    stack = []
    stack.append((vr, vc))
    while stack:
        vr, vc = stack.pop()
        visited[vr][vc] = 1
        if world[vr][vc] == 1:
            # 8 방향 가능
            for i in range(8):
                wr = vr + dr[i]
                wc = vc + dc[i]
                if wr in range(h) and wc in range(w) and not visited[wr][wc] and world[wr][wc] == 1:
                    stack.append(((wr, wc)))

# 상하좌우 및 대각선까지 8방향1
dr = (0, 0, 1, -1, 1, 1, -1, -1)
dc = (1, -1, 0, 0, 1, -1, 1, -1)

while True:
    w, h = map(int, input().split())
    # 마지막 입력값 0 0
    if not w and not h:
        break
    world = [list(map(int, input().split())) for _ in range(h)]
    visited = [[0] * w for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            dfs(i, j)
    print(cnt)