S = [[] for _ in range(5)]
for i in range(5):
  S[i] = input()

S_new = []
for i in range(15):
  for j in range(5):
    try:
      S_new += S[j][i]
    except:
      pass
print(''.join(S_new))