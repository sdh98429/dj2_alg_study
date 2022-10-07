N = int(input())
S = [0] * N
for i in range(N):
  S[i] = int(input())

One = [0] * N
Two = [0] * N

One[0] = S[0]
if N > 1:
  One[1] = S[0] + S[1]
  Two[1] = S[1]
  
  for i in range(2, N):
    One[i] = Two[i-1] + S[i]
    Two[i] = max(Two[i-2]+S[i], One[i-2]+S[i])
print(max(One[N-1], Two[N-1]))
