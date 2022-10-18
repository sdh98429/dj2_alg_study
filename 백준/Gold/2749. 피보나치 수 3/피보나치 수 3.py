N = int(input())
N = N%(15*10**5)
F = [0, 1, 1]
for i in range(2, N+1):
  F[i%3] = (F[(i+1)%3] + F[(i+2)%3]) % 1000000
print(F[N%3])