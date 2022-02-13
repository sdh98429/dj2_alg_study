# !! 거리두기 확인하기, 오랜만의 bfs
# 81302

# places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
from collections import deque

def bfs(i, j, visited, matrix):
    q = deque()
    q.append((i, j, 0))
    visited[i][j] = 1
    while q:
        vr, vc, dist = q.popleft()
        for m in move:
            wr, wc = vr + m[0], vc + m[1]
            if wr in range(5) and wc in range(5) and not visited[wr][wc] and (matrix[wr][wc] != 'X') and dist < 2:
                visited[wr][wc] = 1
                if matrix[wr][wc] == 'P':
                    return -1
                q.append((wr, wc, dist + 1))


move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def solution(places):
    answer = []

    for place in places:
        safe = 1
        matrix =[[0] * 5 for _ in range(5)]
        visited = [[0]*5 for _ in range(5)]
        for i in range(5):
            for j in range(5):
                matrix[i][j] = place[i][j]

        for i in range(5):
            for j in range(5):
                if matrix[i][j] == 'P':
                    if bfs(i, j, visited, matrix) == -1:
                        safe = 0
                        break
        answer.append(safe)
    return answer



# places	result
# [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]	[1, 0, 1, 1, 1]