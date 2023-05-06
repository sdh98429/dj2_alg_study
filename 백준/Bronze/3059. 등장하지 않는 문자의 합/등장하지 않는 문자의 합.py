T = int(input())

for tc in range(T):
  S = input()
  tot = sum(list(i for i in range(65, 91)))
  for s in set(S):
    tot -= ord(s)
  print(tot)