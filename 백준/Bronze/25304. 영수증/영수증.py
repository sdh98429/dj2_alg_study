X = int(input())

T = int(input())
for tc in range(1, T+1):
  a, b = map(int, input().split())
  X -= a*b
print('Yes' if not X else 'No')