N = int(input())
for tc in range(N):
  x, y = map(int, input().split())
  A, B = x, y
  while B:
    A, B = B, A%B
  print(x*y//A)