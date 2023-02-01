import sys
input = sys.stdin.readline

P = [False, False] + [True] * 10000

for i in range(2, int(10000**0.5)+1):
  if P[i]:
    j = 2
    while i*j in range(len(P)):
      P[i*j]= False
      j += 1

T = int(input())

for tc in range(T):
  n = int(input())
  for i in range(n//2, -1, -1):
    if P[i] and P[n-i]:
      print(i, n-i)
      break