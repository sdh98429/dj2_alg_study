while True:
  S = input()
  if S == '0':
    break
  for i in range(len(S)):
    if S[i] != S[len(S)-i-1]:
      print('no')
      break
  else:
    print('yes')