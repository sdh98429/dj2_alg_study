tot = 0
max_tot = 0
for _ in range(10):
  down, up = map(int, input().split())
  tot += (up-down)
  if max_tot < tot:
    max_tot = tot
print(max_tot)