N = int(input())
L = []

for _ in range(N):
  L.append(list(map(int, input().split())))
L.sort(key=lambda x:(x[1], x[0]))
for l in L:
  print(*l)