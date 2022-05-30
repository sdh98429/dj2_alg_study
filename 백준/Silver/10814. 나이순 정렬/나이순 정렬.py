N = int(input())
L = [0] * N
for i in range(N):
    L[i] = (input().split(), i)
L.sort(key = lambda x : (int(x[0][0]), x[1]) )

for l in L:
    print(' '.join(l[0]))