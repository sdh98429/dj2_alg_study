N = int(input())
S = []

for _ in range(N):
  tot = 0
  L = list(map(int, input().split()))
  L.sort()
  if L[0] == L[2]:
    tot = 10000 + 1000 * L[0]
  elif L[0] == L[1] or L[1] == L[2]:
    tot = 1000 + 100 * L[1]
  else:
    tot = L[2] * 100
  S.append(tot)

print(max(S))