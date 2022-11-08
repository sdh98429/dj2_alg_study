N = int(input())
L = []
for i in range(N):
  L.append(list(map(int, input().split())))

for i in range(N):
  order = 1
  for j in range(N):
    if L[j][0] > L[i][0] and L[j][1] > L[i][1]:
      order += 1
  print(order, end=" ")