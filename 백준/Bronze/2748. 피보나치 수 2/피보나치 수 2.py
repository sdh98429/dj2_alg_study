N = int(input())
F = [0, 1] + [0] * N
for i in range(N):
    F[i+2] = F[i+1] + F[i]
print(F[N])