# ! RGB 거리, 색깔 별로 가격 저장

N = int(input())

past_cost = [0, 0, 0] # 바로 전 집 색깔별 최소 가격 R, G, B
now_cost = [0, 0, 0] # 현재 집 색깔별 최소 가격

for _ in range(N):
    R, G, B = map(int, input().split())
    now_cost[0] = min(past_cost[1]+G, past_cost[2] +B) # G, B 색상 각각 칠해진 경우의 최소 가격
    now_cost[1] = min(past_cost[0]+R, past_cost[2] +B) # 나머지 두 색상 칠해진 경우 최소 가격
    now_cost[2] = min(past_cost[0]+R, past_cost[1] +G)
    past_cost = now_cost.copy() # 현재 가격을 전 집 가격 배열로 저장

print(min(now_cost)) # 최소 가격