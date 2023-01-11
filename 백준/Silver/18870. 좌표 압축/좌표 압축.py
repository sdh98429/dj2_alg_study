import sys
input = sys.stdin.readline

N = int(input())
X_pre = list(map(int, input().split()))

X = []
for i, x in enumerate(X_pre):
  X.append((x, i))

X.sort()

tmp = X[0][0]
tmp_ind = 0

X_last = []
for i in range(N):
  if X[i][0] != tmp:
    tmp_ind += 1
  X_last.append((X[i][1], tmp_ind))
  tmp = X[i][0]
X_last.sort()

for x in X_last:
  print(x[1], end=" ")