max_score = 0
winner = 0

for i in range(1, 6):
  L = list(map(int, input().split()))
  if sum(L) > max_score:
    max_score = sum(L)
    winner = i
print(winner, max_score)