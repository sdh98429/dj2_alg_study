# 나무 탈출
# 입력값이 많아 sys.stdin.readline 필요
# 리프 노드인지 확인하고, 루트 노드까지와의 거리의 합이 홀짝

import sys
input = sys.stdin.readline

def BFS(r = 1):
    global tot
    visited[r] = 1
    q = []
    q.append(r)
    while q:
        v = q.pop()
        # 리프노드일 가능성
        leaf = 1
        for w in double[v]:
            if not visited[w]:
                q.append(w)
                visited[w] = visited[v] + 1
                # 자식 노드가 있으니 리프 노드 아님
                leaf = 0
        else:
            # 리프 노드라면 루트노드까지의 거리를 더해줌
            if leaf:
                tot += visited[v] - 1

N = int(input())
double = [[] for _ in range(N+1)]
visited = [0] * (N+1)
for _ in range(N-1):
    a, b = map(int, input().split())
    double[a].append(b)
    double[b].append(a)
tot = 0
BFS()
if tot % 2:
    print('Yes')
else:
    print('No')