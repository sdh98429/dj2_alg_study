T = int(input())
for tc in range(1, T+1):
  S, N = input().split('-')
  tot_S = 0
  for i in range(len(S)):
    tot_S += (ord(S[i])-65) * (26 ** (len(S)-1-i))
  tot_N = int(N)
  if abs(tot_S-tot_N) <= 100:
    print('nice')
  else:
    print('not nice')