N, M = map(int, input().split())
A = list(map(int, input().split()))

start = 0
end = 1
ans = 0
prefix_sum = A[0]
while end <= N:
  if prefix_sum > M:
    prefix_sum -= A[start]
    start += 1
  elif prefix_sum < M:
    if end < N:
      prefix_sum += A[end]
    end += 1
  else:
    ans += 1

    if end < N:
      prefix_sum += A[end]
    end += 1
print(ans)
    