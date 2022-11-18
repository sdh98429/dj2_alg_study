import sys
from itertools import combinations

input = sys.stdin.readline

while True:
  L = list(map(int, input().split()))
  if L[0]:
    C = combinations(L[1:], 6)
    for c in C:
      print(*c)
    print()
  else:
    break