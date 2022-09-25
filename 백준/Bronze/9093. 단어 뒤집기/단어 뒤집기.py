T = int(input())

for tc in range(1, T+1):
  S = input().split()
  for s in S:
    print(s[::-1], end=" ")
  print()