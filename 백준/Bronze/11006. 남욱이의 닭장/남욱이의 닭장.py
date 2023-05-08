T = int(input())

for tc in range(T):
  N, M = map(int, input().split())
  print(2*M-N, N-M)