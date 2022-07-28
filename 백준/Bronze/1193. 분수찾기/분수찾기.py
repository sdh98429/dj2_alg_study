X = int(input())

for x in range(10000):
  if x*(x+1)/2 >= X:
    A = int(X-x*(x-1)/2)
    B = int(x+1-X+x*(x-1)/2)
    print("%d/%d"%(B, A)) if x%2 else print("%d/%d"%(A, B))
    break