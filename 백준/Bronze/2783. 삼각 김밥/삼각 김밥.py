L = []
L.append(list(map(int, input().split())))
N = int(input())
for _ in range(N):
  L.append(list(map(int, input().split())))

tot_min = 987654321

for x, y in L:
  tot = x * (1000/y)
  if tot_min > tot:
    tot_min = tot
print(tot_min)