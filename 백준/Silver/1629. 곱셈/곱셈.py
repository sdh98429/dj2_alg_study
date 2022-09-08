# 분할 정복
def DivideAndConquer(a, b, c):
  if b == 1:
    return a%c
  elif b%2 == 1:
    return ((DivideAndConquer(a, b//2, c)**2)*a)%c
  elif b%2 == 0:
    return (DivideAndConquer(a, b//2, c)**2)%c
    
print(DivideAndConquer(*map(int, input().split())))
  