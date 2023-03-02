def Rev(N):
  R = int(''.join(list(str(N))[::-1]))
  return(R)

X, Y = input().split()
print(Rev(Rev(X) + Rev(Y)))