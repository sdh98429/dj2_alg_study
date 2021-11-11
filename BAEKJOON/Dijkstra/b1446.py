# Dijkstra ! 지름길
# Dijkstra 대신 dfs로 모든 지름길을 선택하거나 선택하지 않는 방식으로 해결
def dfs(ind, dist, real): # 선택하는 지름길의 번호, 현재 위치, 실제 이동한 거리
    global min_r
    if dist > D: # 지름길 도착 지점이 최종 목적지를 앞질렀으면 실패
        return

    if ind == N:
        real += D - dist
        if real < min_r:
            min_r = real
        return

    if dist <= road[ind][0]: # 지름길을 선택하는 경우
        dfs(ind+1, road[ind][1], real+road[ind][2] + road[ind][0]-dist)
        # 지름길 선택안하는 경우
    dfs(ind+1, dist, real)

N, D = map(int, input().split())

road = []
for _ in range(N):
    road.append(list(map(int, input().split())))
# 지름길 시작 지점 거리순으로 정렬
road.sort()
min_r = 987654321
dfs(0, 0, 0)
print(min_r)