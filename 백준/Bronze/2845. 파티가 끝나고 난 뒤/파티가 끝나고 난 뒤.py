L, P = map(int, input().split())
W = list(map(int, input().split()))
for w in W:
  print(w-L*P, end=" ")