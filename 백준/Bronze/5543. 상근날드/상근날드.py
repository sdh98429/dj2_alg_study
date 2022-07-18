H = 9999
D = 9999
for _ in range(3):
    h = int(input())
    if h < H:
        H = h
for _ in range(2):
    d = int(input())
    if d < D:
        D = d
print(H+D-50)
      