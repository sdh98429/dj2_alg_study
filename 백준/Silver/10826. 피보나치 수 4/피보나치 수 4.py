N = int(input())
L = [0, 1, 1] + [0] * (N+10)
L[1] = 1
for i in range(3, N+2):
  L[i] = L[i-1] + L[i-2]
print(L[N])