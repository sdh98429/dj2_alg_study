N = int(input())

L = [0] * (N+1)

for i in range(1, N+1):
  S = i + sum(map(int, list(str(i))))
  if S in range(N+1) and not L[S]:
    L[S] = i

print(L[N])