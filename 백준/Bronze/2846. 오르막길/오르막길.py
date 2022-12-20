N = int(input())
P = list(map(int, input().split()))

max_h = 0
h = 0
before = P[0]

for p in P[1:]:
  if before < p:
    h += p - before
    if max_h < h:
      max_h = h
    before = p
  else:
    h = 0
    before = p
print(max_h)