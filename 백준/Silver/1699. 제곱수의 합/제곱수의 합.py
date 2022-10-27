N = int(input())
DP = [987654321] * (N+1)

for i in range(1, N+1):
  if not i ** 0.5 %1:
    DP[i] = 1
  else:
    for j in range(1, int(i**0.5)+1):
      DP[i] = min(DP[i], 1+DP[i-j**2])
print(DP[-1])