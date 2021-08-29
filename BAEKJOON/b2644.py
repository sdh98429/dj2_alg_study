
def dfs(v, d = 1):
    visited[v] = d
    for w in adj_list[v]:
        if not visited[w]:
            dfs(w, visited[v] + 1)

N = int(input())
S, G = list(map(int, input().split()))
M =int(input())
XY = [list(map(int, input().split(' '))) for _ in range(M)]

adj_list = [[] for _ in range(N+1)]
visited = [0] * (N+1)


for m in range(M):
    adj_list[XY[m][0]].append(XY[m][1])
    adj_list[XY[m][1]].append(XY[m][0])

dfs(S)
print(visited[G]-1)    