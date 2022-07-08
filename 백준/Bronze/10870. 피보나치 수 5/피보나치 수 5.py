N = int(input())

F = [0, 1] + [0] * (N-1)

for i in range(2, N+1):
  F[i] = F[i-1] + F[i-2]

print(F[N])