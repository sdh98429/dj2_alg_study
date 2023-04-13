N, W, H = map(int, input().split())
max_len = int((W ** 2 + H ** 2)**0.5)
for _ in range(N):
  if int(input()) > max_len:
    print('NE')
  else:
    print('DA')