T = int(input())
for tc in range(T):
  H, W, N = map(int ,input().split())
  w = (N-1)//H+1
  h = (N-1)%H+1
  print(h * 100 + w)