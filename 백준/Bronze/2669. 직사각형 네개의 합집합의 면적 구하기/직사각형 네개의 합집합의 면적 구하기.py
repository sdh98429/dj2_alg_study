L = [[0] * 100 for _ in range(100)]

for _ in range(4):
  LX, LY, RX, RY = map(int, input().split())
  for i in range(LX, RX):
    for j in range(LY, RY):
      L[i][j] = 1

ans = 0
for i in range(100):
  ans += sum(L[i])

print(ans)