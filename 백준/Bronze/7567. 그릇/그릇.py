S = input()
tot = 0
before = ''
for s in S:
  if before != s:
    tot += 10
  else:
    tot += 5
  before = s
print(tot)