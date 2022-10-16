T = int(input())
for tc in range(T):
  N = int(input())
  D = dict()
  for _ in range(N):
    name, cloth = input().split()
    try:
      D[cloth] +=1
    except:
      D[cloth] = 1
  ans = 1
  for key, value in D.items():
    ans *= (value+1)
  print(ans-1)