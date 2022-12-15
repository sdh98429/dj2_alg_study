N, K = map(int, input().split())
L = list(map(int, input().split()))
tot = sum(L[:K])
max_tot =  -987654321
if tot > max_tot:
  max_tot = tot
for i in range( N-K):
  tot += (L[i+K] - L[i])
  if tot > max_tot:
    max_tot = tot
print(max_tot)