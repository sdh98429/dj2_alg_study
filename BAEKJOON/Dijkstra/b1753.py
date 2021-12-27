# Dijkstra !! 최단 경로
# 문제 조건 잘 읽기, 두 점 사이에 하나의 경로만 있는 것이 아님
import sys

def Dijkstra():
    U = [0] * (V+1)
    U[K] = 1 # 틀린 원인 1, 시작점이 1이 아닐 수도 있음

    D = [987654321] * (V+1)
    D[K] = 0
    for pair in link[K]:
        D[pair[0]] = min(D[pair[0]], pair[1]) # 틀린 원인 2, 무조건 덮어씌우는 것이 아니라 시작점과 다른 점 사이에 경로가 2개 이상 있을 수 있음. 더 작은 거리로 정해야 함

    while sum(U) != V: # 모두 방문한 경우
        min_w = 987654321
        w = -1

        for i in range(1, V+1):
            if not U[i] and D[i] < min_w:
                min_w = D[i]
                w = i

        if w == -1: # 경로가 없는 점만 남았을 때
            for i in range(1, V+1):
                if D[i] == 987654321: # INF로 값 바꿔주기
                    D[i] = 'INF'
            break

        U[w] = 1 # 방문처리

        for v in link[w]:
            D[v[0]] = min(D[v[0]], D[w] + v[1])

    for i in range(1, V+1):
        print(D[i])


V, E = map(int, input().split())
K = int(input())
link =[[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().rstrip().split()) # 개행문자 없애주기
    link[u].append((v, w)) # 인접행렬로 하면 메모리 너무 커지므로 연결된 간선들의 번호만 저장

Dijkstra()
