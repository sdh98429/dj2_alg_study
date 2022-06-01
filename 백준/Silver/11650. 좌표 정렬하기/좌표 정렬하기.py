N = int(input())

L = [0] * N
for i in range(N):
    L[i] = list(map(int, input().split()))

L.sort(key = lambda x : (x[0], x[1]))
for l in L:
    print(*l)