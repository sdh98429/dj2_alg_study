S = input()
tot = 0
for s in S:
  if s in ['a', 'e', 'i', 'o', 'u']:
    tot += 1
print(tot)