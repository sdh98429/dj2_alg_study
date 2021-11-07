# !! MST 게임
# KRUSKAL로 해결

import sys
input = sys.stdin.readline

def find_set(x):
    if x == p[x]:
        return x
    else:
        return find_set(p[x])

def union(x, y):
    p[find_set(y)] = find_set(x)

def MST_KRUSKAL():
    tot = 0
    cnt = 0
    first = True
    for eg in EDGE:
        W, n1, n2 = eg
        if W and find_set(n1) != find_set(n2):
            union(n1, n2)
            tot += W
            cnt += 1
            if first:
                eg[0] = 0
                first = False

        if cnt == N-1:
            return tot
    else:
        return 0


N, M, K = map(int, input().split())

EDGE = [[] for _ in range(M)]

for i in range(M):
    a, b = map(int, input().split())
    EDGE[i] = [i+1, a, b]



for k in range(K):
    p = [i for i in range(N + 1)]
    ans = MST_KRUSKAL()
    if ans:
        print(ans, end=' ')
    else:
        for z in range(K-k):
            print(0, end=' ')
        break
