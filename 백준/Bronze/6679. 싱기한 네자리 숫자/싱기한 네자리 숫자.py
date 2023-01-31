def notation(N, base):
  tot = 0
  while N:
    tot += N%base
    N //= base
  return tot

for i in range(1000, 10000):
  if notation(i, 10) == notation(i, 12):
    if notation(i, 12) == notation(i, 16):
      print(i)