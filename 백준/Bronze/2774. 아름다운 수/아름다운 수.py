T = int(input())
for tc in range(T):
  S = input()
  beauty = 0
  A = set()
  for s in S:
    A.add(s)
  print(len(A))