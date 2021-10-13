from collections import deque

def bfs(i, j):
    global matrix
    q = deque([[i,j]])
    cl = matrix[i][j]
    flag = 0
    while q:
        v1, v2 = q.popleft()
        if matrix[v1][v2] != 'X':
            if cl == matrix[v1][v2]:
                matrix[v1][v2] = 'X'
                flag = 1
                for d in dd:
                    if 0 <= v1 + d[0] < N and 0 <= v2 + d[1] < N:
                        q.append([v1+d[0], v2+d[1]])
    return flag

def bfs2(i, j):
    global matrix2
    q = deque([[i,j]])
    cl = matrix2[i][j]
    flag = 0
    while q:
        v1, v2 = q.popleft()
        if matrix2[v1][v2] != 'X':
            if cl == matrix2[v1][v2]:
                matrix2[v1][v2] = 'X'
                flag = 1
                for d in dd:
                    if 0 <= v1 + d[0] < N and 0 <= v2 + d[1] < N:
                        q.append([v1+d[0], v2+d[1]])
    return flag

N = int(input())
matrix = [[] for _ in range(N)]
matrix2 = [[] for _ in range(N)]

no = 0
bl = 0

dd = [[0, 1], [1, 0], [0, -1], [-1, 0]]

for m in range(N):
    one = list(input())
    matrix[m] = one
    for o in one:
        if o == 'G':
            o = 'R'
        matrix2[m].append(o)

for i in range(N):
    for j in range(N):
        no += bfs(i,j)
        bl += bfs2(i, j)

print(no, end=' ')
print(bl)