D = dict()
N = int(input())
for _ in range(N):
  B = input()
  try:
    D[B] += 1
  except:
    D[B] = 1
max_cnt = 0
candidate = []
for name, cnt in D.items():
  if cnt > max_cnt:
    candidate = [name]
    max_cnt = cnt
  elif cnt == max_cnt:
    candidate += [name]
candidate.sort()
print(candidate[0])