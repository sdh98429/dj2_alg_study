N = int(input())

for _ in range(N):
  word_1, word_2 = list(input().split())
  word_1 = sorted(word_1)
  word_2 = sorted(word_2)
  if word_1 == word_2:
    print('Possible')
  else:
    print('Impossible')