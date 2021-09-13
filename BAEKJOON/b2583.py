def bfs(ni, nj):
    q = [[ni, nj]]
    area = 0
    while q:
        v = q.pop()
        if not visited[v[0]][v[1]]:
            visited[v[0]][v[1]] = 1
            area += 1
            if v[0] + 1 < M and not visited[v[0]+1][v[1]]:
                q.append([v[0]+1, v[1]])
            if v[1] + 1 < N and not visited[v[0]][v[1]+1]:
                q.append([v[0], v[1]+1])
            if v[0] - 1 >= 0 and not visited[v[0]-1][v[1]]:
                q.append([v[0]-1, v[1]])
            if v[1] - 1 >= 0 and not visited[v[0]][v[1]-1]:
                q.append([v[0], v[1]-1])
    areas.append(area)

M, N, K = list(map(int, input().split()))
XY = [[] for _ in range(K)]

for a in range(K):
    XY[a] = list(map(int, input().split()))

matrix = [[0] * N for _ in range(M)]
visited = [[0] * N for _ in range(M)]
num = 0
areas = []

for b in range(K):
    for i in range(XY[b][0], XY[b][2]):
        for j in range(XY[b][1], XY[b][3]):
            visited[j][i] = 1

for i in range(M):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j)
            num += 1
areas.sort()
print(num)
for ar in areas:
    print(ar, end=' ')
"""
5 7 3
0 2 4 4
1 1 2 5
4 0 6 2
"""