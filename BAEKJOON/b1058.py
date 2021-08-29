''' 저처럼 안되는 분들을 위한 반례
6
NYYNYN
YNYNNN
YYNYNN
NNYNNN
YNNNNY
NNNNYN
'''

def dfs2(p, order = 0):
    global visited
    visited[p] = 1
    if order == 2:
        return
    for f in adj_list[p]:
        dfs2(f, order + 1)


N = int(input())
matrix = [list(input()) for _ in range(N)]

adj_list = [[] for _ in range(N+1)]

for i in range(N):
    for j in range(N):
        if matrix[i][j] == 'Y':
            adj_list[i+1] += [j+1]
            adj_list[j+1] += [i+1]


max_f = 0
for people in range(1, N+1):
    visited = [0] * (N+1)
    dfs2(people)
    if max_f < sum(visited) - 1:
        max_f = sum(visited) - 1
print(max_f)
