import sys
input = sys.stdin.readline

from collections import deque

def bfs():
    global matrix, tomato

    time = 0
    while tomato:
        vr, vc, vtime = tomato.popleft()
        if not matrix[vr][vc] or not vtime:
            if vtime > time:
                time = vtime
            matrix[vr][vc] = 1
            for d in range(4):
                wr = vr + dr[d]
                wc = vc + dc[d]
                if wr in range(N) and wc in range(M):
                    tomato.append((wr, wc, vtime+1))
    return time

M, N = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]


dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

tomato = deque()
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 1:
            tomato.append((i, j, 0))

result = bfs()

for i in range(N):
    for j in range(M):
        if not matrix[i][j]:
            result = -1
            break
    else:
        continue
    break

print(result)
