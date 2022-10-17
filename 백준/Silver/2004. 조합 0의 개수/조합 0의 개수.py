def FiveCnt(K):
  cnt = 0
  while K:
    cnt += K//5
    K //= 5
  return cnt

def TwoCnt(K):
  cnt = 0
  while K:
    cnt += K//2
    K //= 2
  return cnt

N, M = map(int, input().split())
print(min(FiveCnt(N)-FiveCnt(N-M)-FiveCnt(M), TwoCnt(N)-TwoCnt(N-M)-TwoCnt(M)))
