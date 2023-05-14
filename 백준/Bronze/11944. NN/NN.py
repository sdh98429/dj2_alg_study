N, M = map(int, input().split())
str_N = list(str(N))
length = min(len(str(N))*N, M)
for i in range(length):
  print(str_N[i%len(str_N)], end='')
  