tot = 0

for _ in range(10):
  a = int(input())
  if abs(100 - a - tot) <= abs(100 -tot):
    tot += a
  else:
    print(tot)
    break
else:
  print(tot)