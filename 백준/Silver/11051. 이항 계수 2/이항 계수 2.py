import math
N, K = map(int, input().split())

num = 1
for i in range(N-K+1, N+1):
  num *= i

div = 1
for j in range(1, K+1):
  div *= j


print((num//div)%10007)