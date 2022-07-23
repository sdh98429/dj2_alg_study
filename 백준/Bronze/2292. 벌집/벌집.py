N = int(input())
for i in range(int(N**0.5)+1):
  if N-1 <= 6 * i * (i+1) / 2:
    print(i+1)
    break