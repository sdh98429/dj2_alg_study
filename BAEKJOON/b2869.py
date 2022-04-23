# 달팽이는 올라가고 싶다

A, B, V = map(int, input().split())
print((V-A)//(A-B)+2 if (V-A)%(A-B) else (V-A)//(A-B)+1)