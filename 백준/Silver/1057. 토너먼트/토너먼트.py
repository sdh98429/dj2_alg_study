N, A, B = map(int, input().split())
round = 0
while A != B:
  round += 1
  A = A//2 + A%2
  B = B//2 + B%2
print(round)