N = int(input())

tot = 0
for i in range(1, N+1):
  for j in range(i, N+1):
    if i*j <= N:
      tot += 1
print(tot)