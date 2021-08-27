def bfs(v):
    q = [v]
    while q:
        v = q.pop(0)
        if not visited[v]:
            visited[v] = 1
            for w in range(1, N+1):
                if not visited[w] and matrix[v][w]:
                    q.append(w)



N = int(input())
E = int(input())

visited = [0] * (N+1)
matrix = [[0] * (N+1) for _ in range(N+1)]

for _ in range(E):
    i, j = list(map(int, input().split()))
    matrix[i][j] = 1
    matrix[j][i] = 1

bfs(1)
print(sum(visited) - 1) # 1번 컴퓨터 제외