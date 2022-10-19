
N = int(input())
L = list(map(int, input().split()))
M = int(input())

start, end = 0, max(L)
while start <= end:
  mid = (start + end) // 2
  tot = 0
  for l in L:
    if l >= mid:
      tot += mid
    else:
      tot += l
  if tot <= M:
    start = mid + 1
  else:
    end = mid - 1

print(end)
