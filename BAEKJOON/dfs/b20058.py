# !!! dfs 마법사 상어와 파이어스톰
# 이것은 수학문제... (r, c) 부터 시작하는 N * N 정사각형 안에서 시계방향으로 90도를 회전시키면
# (r+i, c+j) -> (r+j, c+N-1-j)로 좌표가 이동함
# 모든 작은 정사각형 부분들의 좌표를 회전시킨후,
# BFS()로 인접한 얼음의 개수가 2개 이하면 1 감소시킨 fire_mat를 반환한다.
# 그리고 모든 좌표에서 BFS_ice()를 써 제일 큰 얼음 덩어리를 확인해준다.
# BFS를 BFS()와 BFS_ice()에서 중복해서 쓰는 기분인데 줄이는 법을 모르겠다.

import sys
input = sys.stdin.readline

# 얼음 녹이는 코드
def BFS(new_mat):
    fire_mat = [[0] * M for _ in range(M)] # 돌리고 녹인 후의 지도
    q = []
    q.append((0, 0))
    visited[0][0] = 1
    while q:
        vr, vc = q.pop(0)
        adj = 0 # 인접한 얼음 있는지 확인
        for m in range(4):
            wr = vr + dr[m]
            wc = vc + dc[m]
            if wr in range(M) and wc in range(M):
                if not visited[wr][wc]:
                    q.append((wr, wc))
                    visited[wr][wc] = 1
                if new_mat[wr][wc]: # 만약 얼음이 0이 아니라면 인접한 얼음 수 추가
                    adj += 1

        if adj >= 3: # 인접한 얼음이 3 개 이상
            fire_mat[vr][vc] = new_mat[vr][vc]
        else: # 인접한 얼음이 2개 이하일 때 1 빼준다. 0일 때는 빼주면 안됨
            fire_mat[vr][vc] = new_mat[vr][vc] - 1 if new_mat[vr][vc] else new_mat[vr][vc]
    return fire_mat # 전자렌지 돌린 지도

# si, sj에서 시작하는 가장 큰 얼음 덩어리를 구한다
def BFS_ice(mat, si, sj):
    global visited_ice, max_ice
    q = []
    q.append((si, sj))
    if not mat[si][sj]: # 얼음이 없다면 돌아간다
        return
    else:
        visited_ice[si][sj] = 1
        cnt = 1 # 얼음 덩어리 크기
        while q:
            vr, vc = q.pop(0)
            for m in range(4):
                wr = vr + dr[m]
                wc = vc + dc[m]
                # 방문하지 않았고 얼음이 있는 곳만 추가
                if wr in range(M) and wc in range(M) and not visited_ice[wr][wc] and mat[wr][wc]:
                    q.append((wr, wc))
                    visited_ice[wr][wc] = 1
                    cnt += 1
        # 현재 얼음 덩어리가 기존 얼음 덩어리보다 크면 바꿔줌
        if cnt > max_ice:
            max_ice = cnt

N, Q = map(int, input().split())
M = 2 ** N
mat = [list(map(int, input().split())) for _ in range(M)]
L = list(map(int, input().split()))

dr = (1, -1, 0, 0)
dc = (0, 0, 1, -1)

# 모든 파이어스톰 실행
for l in L:
    new_mat = [[0] * M for _ in range(M)] # 회전 후 저장할 행렬
    visited = [[0] * M for _ in range(M)] # BFS() 방문 표시용
    S = 2 ** l # 작은 사각형 크기
    # 각각의 사각형들에 대해
    for r in range(M//S):
        for c in range(M//S):
            # 작은 사각형 내부의 모든 점에 대해
            for i in range(S):
                for j in range(S):
                    # 회전 함수, 수직하는 기울기의 곱은 -1이 되는 걸 이용해 구함
                    new_mat[S * r + j][S * c + S - 1 - i] = mat[S * r + i][S * c + j]
    # new_mat를 녹여 mat에 담음
    mat = BFS(new_mat)


max_ice = 0 # 최대 얼음 덩어리 크기
visited_ice = [[0] * M for _ in range(M)] # BFS_ice() 방문 표시용
for i in range(M):
    for j in range(M):
        if not visited_ice[i][j]: # 방문하지 않은 시작점에 대해서만
            BFS_ice(mat, i, j) # i, j 에서 시작하는 얼음 덩어리 크기 구하기

# 얼음의 개수 합, # 이중리스트의 모든 요소 더해주기
# sum 뒤에 인자를 []를 붙여주면 리스트끼리 더해줄 수 있다. sum 뒤에 인자가 없는 경우는 0을 더해줘서 오류 나는 것
# 출처 : https: // blockdmask.tistory.com / 558
print(sum(sum(mat, [])))
# 가장 큰 얼음 덩어리
print(max_ice)
