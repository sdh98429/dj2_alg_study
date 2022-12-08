N = int(input())
L = list(map(int, input().split()))
tot = 0
score = 0
for l in L:
  if l:
    score += 1
    tot += score
  else:
    score = 0
print(tot)