N, M = map(int, input().split())
T = list(map(int, input().split()))

start = 0
end = max(T)
mid = (start + end) // 2

while mid > start and end > mid:
  wood = 0
  for t in T:
    if mid < t:
      wood += t - mid
      
  if wood < M:
    end = mid
    mid = (start + end ) // 2
  elif wood > M:
    start = mid
    mid = (start + end ) // 2
  else:
    break

print(mid)


