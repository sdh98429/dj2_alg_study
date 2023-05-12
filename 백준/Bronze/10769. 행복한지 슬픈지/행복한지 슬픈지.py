S = list(input())

happy_cnt = 0
sad_cnt = 0

for i in range(len(S)-2):
  s = ''.join(list(S[i:i+3]))

  if s == ':-)':
    happy_cnt += 1
  elif s == ':-(':
    sad_cnt += 1

if happy_cnt or sad_cnt:
  if happy_cnt == sad_cnt:
    print('unsure')
  elif happy_cnt > sad_cnt:
    print('happy')
  else:
    print('sad')
else:
  print('none')