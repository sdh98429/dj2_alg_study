from collections import deque

N, M = map(int, input().split())

cost = [0]*(N+1)
car = [0]*(M+1)
car_park = [0]*(M+1)

empty = [1] * (N+1)
wait = deque()

for i in range(1, N+1):
    cost[i] = int(input())

for i in range(1, M+1):
    car[i] = int(input())

result = 0
for _ in range(2*M):
    k = int(input())
    if k > 0:
        for i in range(1, N+1):
            if empty[i]:
                empty[i] = 0
                car_park[k] = i
                break
        else:
            wait.append(k)
    else:
        result += cost[car_park[-k]] * car[-k]
        empty[car_park[-k]] = 1
        if wait:
            car_park[wait.popleft()] = car_park[-k]
            empty[car_park[-k]] = 0

print(result)