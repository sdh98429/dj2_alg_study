import sys
input = sys.stdin.readline

def mul(X, Y):
  Z = [[0]*N for _ in range(N)]
  for i in range(N):
    for j in range(N):
      ele = 0
      for k in range(N):
        ele += X[i][k] * Y[k][j]
      Z[i][j] = ele%1000
  return Z
      

def power(M, p):
  if p == 1:
    Z = [[0]*N for _ in range(N)]
    for i in range(N):
      for j in range(N):
        Z[i][j] = M[i][j] % 1000
    return Z

  half = power(M, p//2)
    
  if not p%2:
    return mul(half, half)
  else:
    return mul(mul(half, half),A)
  
N, B = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(N)]


ans_mat = power(A, B)
for r in ans_mat:
  print(*r)