T = int(input())

for tc in range(T):
  S = int(input())
  N = int(input())
  for _ in range(N):
    q, p = map(int, input().split())
    S += q * p
  print(S)