N = int(input())

DP = [987654321] * (N+1)
DP[0:2] = [0, 0]
Way = [[] for _ in range(N+1)]
Way[1] = [1]

for i in range(2, N+1):
  op1 = DP[i//3] + 1 if not i%3 else 987654321
  op2 = DP[i//2] + 1 if not i%2 else 987654321
  op3 = DP[i-1] + 1
  DP[i] = min(op1, op2, op3)
  Way[i] = (([i] + Way[i//3]) if DP[i]==op1 else (([i] + Way[i//2]) if DP[i]==op2 else ([i] + Way[i-1])))
print(DP[N])
print(*Way[N])
