N = int(input())

for i in range(N):
  print(' '*(N-1-i), end="")
  for j in range(2*i+1):
    if j%2:
      print(' ', end="")
    else:
      print('*', end="")
  print()