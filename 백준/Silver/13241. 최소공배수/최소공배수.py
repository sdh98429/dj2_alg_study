def GCD(x, y):
  while y:
    x, y = y, x%y
  return x

A, B = map(int, input().split())
print(A*B//GCD(A,B))