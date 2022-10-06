K, N = map(int, input().split())

Lan = []
for _ in range(K):
  Lan += [int(input())]

start, end = 1, max(Lan)

while start <= end:
  lines = 0
  mid = (start + end)//2

  for lan in Lan:
    lines += lan//mid

  if lines >= N:
    start = mid + 1
  else:
    end = mid - 1
print(end)