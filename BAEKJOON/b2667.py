"""
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
"""
from collections import deque
def bfs(ni, nj):
    area = 0
    q = deque([[ni, nj]])
    while q:
        v = q.popleft()
        if visited[v[0]][v[1]]:
            area += 1
            visited[v[0]][v[1]] = 0
            if v[0] + 1 < T and visited[v[0]+1][v[1]]:
                q.append([v[0]+1, v[1]])
            if v[1] + 1 < T and visited[v[0]][v[1]+1]:
                q.append([v[0], v[1]+1])
            if v[0] - 1 >= 0 and visited[v[0]-1][v[1]]:
                q.append([v[0]-1, v[1]])
            if v[1] - 1 >= 0 and visited[v[0]][v[1]-1]:
                q.append([v[0], v[1]-1])
    return area


T = int(input())

visited = [list(map(int, input())) for _ in range(T)]

house = 0
areas = []

for i in range(T):
    for j in range(T):
        if visited[i][j]:
            house += 1
            areas.append(bfs(i,j))

print(house)
areas.sort()
for a in areas:
    print(a)
