N = int(input())

if N <= 0:
  DP = [1] + [0] * (abs(N)+1)
  for i in range(2, abs(N)+2):
    DP[i] = DP[i-2] - DP[i-1]
    if DP[i] >= 1000000000:
      DP[i] -= 1000000000
    elif DP[i] <= -1000000000:
      DP[i] += 1000000000
  if DP[abs(N)+1] > 0:
    print(1)
  elif DP[abs(N)+1] < 0:
    print(-1)
  else:
    print(0)
  print(abs(DP[abs(N)+1]))
else:
  DP = [0, 1] + [0] * abs(N)
  for i in range(2, N+1):
    DP[i] = (DP[i-1] + DP[i-2]) % 1000000000
  print(1)
  print(DP[N])