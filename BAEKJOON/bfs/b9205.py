# bfs ! 맥주 마시면서 걸어가기
# 맥주 20개 * 개당 50m = 1000m 이니 편의점 도착 때마다 1000m를 새로 갈 수 있음
# bfs로 편의점을 차례로 방문하면서 페스티벌에 도착할 수 있는지 확인
from collections import deque

def bfs():
    q = deque()
    q.append((H[0], H[1]))
    while q:
        wr, wc = q.popleft()
        if abs(wr - fest[0]) + abs(wc - fest[1]) <= 1000: # 페스티벌장 도착 가능
            return "happy"

        for i in range(n):
            if not visited[i] and (abs(store[i][0] - wr) + abs(store[i][1] - wc)) <= 1000: # 아직 들리지 않은 편의점이고 현재 위치와 1000m 이내에 있음
                visited[i] = 1
                q.append((store[i][0], store[i][1]))

    else:
        return "sad"

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    H = list(map(int, input().split()))
    store = [[] for _ in range(n)]
    visited = [0] * n # 상하좌우로 이동하는 것이 아니라 편의점 기준으로 움직이니 방문 표시도 편의점 기준
    for i in range(n):
        store[i] = list(map(int, input().split()))
    fest = list(map(int, input().split()))
    print(bfs())