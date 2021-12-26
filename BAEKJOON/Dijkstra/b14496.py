# Dijkstra ! 그대, 그머가 되어
# 다익스트라로 풀어봄
# 치환 불가능한 경우 -1 출력하라는 문구 못 읽어서 계속 틀림
import sys
input = sys.stdin.readline

def Dijkstra(s, link, D):
    global possible
    U = [0] * (N+1)
    U[s] = 1
    for v in link[s]:
        D[v] = 1

    while sum(U) != N:
        min_w = 987654321
        w = -1
        for i in range(1, N+1):
            if not U[i] and D[i] < min_w:
                min_w = D[i]
                w = i
        if w == -1:
            possible = False
            break
        U[w] = 1

        for v in link[w]:
            D[v] = min(D[v], D[w] + 1)



a, b = map(int, input().split())
N, M = map(int, input().split())
link = [[] for _ in range(N+1)]
big = 987654321 # 임의의 큰 수
possible = True # 치환 가능 여부
for i in range(M):
    front, back = map(int, input().split())
    link[front].append(back)
    link[back].append(front)
D = [big] * (N+1)
D[a] = 0
Dijkstra(a, link, D)
if possible:
    print(D[b])
else:
    print(-1)