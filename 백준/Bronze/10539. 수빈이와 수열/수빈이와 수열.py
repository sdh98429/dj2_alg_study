N = int(input())
B = list(map(int, input().split()))

A = []
for i in range(N):
  tot = B[i] *(i+1)
  A.append(tot-B[i-1]*i)
print(*A)