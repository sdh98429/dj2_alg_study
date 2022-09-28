N = int(input())
tot = 0
for _ in range(N):
  tot += int(input())
print('Junhee is cute!' if tot > N//2 else 'Junhee is not cute!')