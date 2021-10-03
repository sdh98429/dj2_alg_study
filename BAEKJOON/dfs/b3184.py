from collections import deque
def bfs(r, c):
    global matrix
    sh = 0
    wo = 0
    q = deque([[r, c]])
    while q:
        v1, v2 = q.popleft()
        if matrix[v1][v2] != '#':
            if matrix[v1][v2] == 'o':
                sh += 1
            elif matrix[v1][v2] == 'v':
                wo += 1
            matrix[v1][v2] = '#'
            for d in dd:
                if 0 <= v1+d[0] < R and 0 <= v2+d[1] < C:
                    q.append([v1+d[0], v2+d[1]])
    if sh > wo:
        return 0, sh
    else:
        return 1, wo


R, C = map(int, input().split())

matrix = [[] for _ in range(R)]
for r in range(R):
    matrix[r] = list(input())

dd = [
    [0, 1], [1, 0], [0, -1], [-1, 0]
]
result = [0, 0]

for i in range(R):
    for j in range(C):
        ind, cnt = bfs(i, j)
        result[ind] += cnt

print(result[0], end=' ')
print(result[1])