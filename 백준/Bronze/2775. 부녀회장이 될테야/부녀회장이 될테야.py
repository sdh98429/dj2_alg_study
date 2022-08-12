max_k = 15
B = [[0] * max_k for _ in range(max_k)]
B[0] = [i for i in range(max_k+1)]

for k in range(1, max_k):
  for n in range(max_k):
    B[k][n] = sum(B[k-1][0:n+1])

T = int(input())
for tc in range(T):
  a, b = int(input()), int(input())
  print(B[a][b])
