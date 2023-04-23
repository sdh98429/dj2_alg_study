T = int(input())

for _ in range(T):
  N = int(input())
  tot_C = 0
  tot_G = 0
  for _ in range(N):
    C, G = map(float, input().split())
    tot_C += C
    tot_G += G * C
  print(int(tot_C))
  print(tot_G/tot_C)