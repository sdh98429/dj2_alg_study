# bfs ! 안전영역
# 시간복잡도에 대한 꿀팁을 얻었다!!
# https://www.acmicpc.net/board/view/46416
# BFS는 큐에서 뺀 후가 아니라 큐에 넣을 때 방문표시를 해야 시간 복잡도가 망가지지 않는다!!

from collections import deque
import sys
input = sys.stdin.readline

def bfs(i, j, h): # 시작하는 위치 i, j, 비의 높이 h
    global now_island # 지금 비의 높이일때 생기는 섬의 개수
    q = deque()

    now_island += 1
    q.append((i, j))
    visited[i][j] = 1
    while q:
        wr, wc = q.popleft()
        # 원래는 이 줄에 방문 표시를 넣었는데, 그러자 시간 복잡도가 높아 통과하지 못했다
        for m in range(4):
            vr = wr + dr[m]
            vc = wc + dc[m]
            if vr in range(N) and vc in range(N) and not visited[vr][vc] and land[vr][vc] > h: # 비에 침수되지 않았고 방문 안했고 범위 안에 있을 때
                q.append((vr, vc))
                visited[vr][vc] = 1 ## 꿀팁 : bfs는 큐에 넣을 때 방문 표시 해주는게 시간 복잡도가 낮음


dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

N = int(input())

land = [[] for _ in range(N)]

max_h = 0
for i in range(N):
    land[i] = list(map(int, input().split()))
    max_h = max(max_h, max(land[i]))

max_island = 0
for h in range(max_h+1): # 모든 비의 높이
    now_island = 0
    visited = [[0]*N for _ in range(N)]
    for i in range(N): # 모든 지역에 대해 섬이 있는지 확인
        for j in range(N):
            if not visited[i][j] and land[i][j] > h:
                bfs(i, j, h)
    if max_island < now_island: # 최대 섬의 개수 확인
        max_island = now_island
print(max_island)