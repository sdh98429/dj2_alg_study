N = int(input())

DP_A = [1] + [0] *N
DP_B = [0] * (N+1)
for i in range(1, N+1):
  DP_A[i] = DP_B[i-1]
  DP_B[i] = DP_A[i-1] + DP_B[i-1]
print(DP_A[N],DP_B[N])