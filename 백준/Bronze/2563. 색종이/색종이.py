Paper = [[0]*100 for _ in range(100)]
T = int(input())

for _ in range(T):
  x, y = map(int, input().split())
  for i in range(x, x+10):
    for j in range(y, y+10):
      try:
        Paper[i][j] = 1
      except:
        pass
tot = 0
for i in range(100):
  for j in range(100):
    tot += Paper[i][j]
print(tot)