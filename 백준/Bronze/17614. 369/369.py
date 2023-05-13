N = int(input())
tot = 0
for i in range(1, N+1):
  for s in list(str(i)):
    if s in ['3','6','9']:
      tot += 1
print(tot)