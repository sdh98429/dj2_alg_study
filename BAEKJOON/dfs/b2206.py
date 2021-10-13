# 2206 벽 부수고 이동하기
# 역대급으로 어려웠던 문제, 벽을 부순 경우와 부수지 않은 경우 각각 visited 2개 만들어 해결
import sys

from collections import deque

def bfs(VR, VC, WALL):
    global ans
    q = deque()
    q.append([VR, VC, WALL])
    visited[VR][VC] = 1
    visited2[VR][VC] = 1
    while q:
        vr, vc, wall = q.popleft()
        if vr == N-1 and vc == M-1:
            if not wall:
                if visited[vr][vc] < ans:
                    ans = visited[vr][vc]
            else:
                if visited2[vr][vc] < ans:
                    ans = visited2[vr][vc]
        for d in move:
            wr = vr + d[0]
            wc = vc + d[1]
            if wr in range(N) and wc in range(M):
                if not visited2[wr][wc] and wall: # 벽을 한 번 부순 경우
                    if not mat[wr][wc]:
                        q.append([wr, wc, 1])
                        visited2[wr][wc] = visited2[vr][vc] + 1
                elif not visited[wr][wc] and not wall: # 벽을 부수지 않은 경우
                    if mat[wr][wc]: # 다음 위치에 벽이 있을 때 부순다
                        q.append([wr, wc, 1])
                        visited2[wr][wc] = visited[vr][vc] + 1
                    else: # 다음 위치가 비어있다
                        q.append([wr, wc, 0])
                        visited[wr][wc] = visited[vr][vc] + 1
    if ans == 987654321:
        ans = -1

N, M = map(int, sys.stdin.readline().split()) # 윤지영님 코드 참고
mat = [list(map(int, list(input()))) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
visited2 = [[0] * M for _ in range(N)]

move = ((0, 1), (0, -1), (1, 0), (-1, 0))
ans = 987654321
bfs(0, 0, 0)
print(ans)