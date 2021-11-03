# bfs 나이트의 이동 pypy3
import sys
input = sys.stdin.readline

from collections import deque

def bfs():
    q = deque()
    visited[si][sj] = 1
    q.append((si, sj, 0))
    while q:
        vr, vc, cnt = q.popleft()
        if vr == ei and vc == ej:
            return cnt

        for m in range(8):
            wr = vr + dr[m]
            wc = vc + dc[m]
            if wr in range(I) and wc in range(I) and not visited[wr][wc]:
                visited[wr][wc] = 1
                q.append((wr, wc, cnt+1))


dr = [2, 2, -2, -2, 1, 1, -1, -1]
dc = [1, -1, 1, -1, 2, -2, 2, -2]

T = int(input())

for tc in range(1, T+1):
    I = int(input())
    si, sj = map(int, input().split())
    ei, ej = map(int,input().split())
    visited = [[0] * I for _ in range(I)]
    print(bfs())