N = int(input())

for i in range(N-1):
  print(' '*(N-1-i), end="")
  print('*', end="")
  print(' '*(2*i-1),end="")
  print('*' if i else '')
print('*'*(2*N-1))