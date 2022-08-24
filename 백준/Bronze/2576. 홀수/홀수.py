min_odd = 987654321
sum_odd = 0
for _ in range(7):
  n = int(input())
  if n%2:
    if n < min_odd:
      min_odd = n
    sum_odd += n

if sum_odd:
  print(sum_odd)
  print(min_odd)
else:
  print(-1)
    