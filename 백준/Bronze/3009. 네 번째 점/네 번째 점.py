X = dict()
Y = dict()
for _ in range(3):
    x, y = map(int ,input().split())
    if X.get(x):
      del X[x]
    else:
        X[x] = True
    if Y.get(y):
      del Y[y]
    else:
        Y[y] = True
print(*list(X.keys()), *list(Y.keys()))
    