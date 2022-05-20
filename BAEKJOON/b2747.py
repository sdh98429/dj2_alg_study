# 피보나치 수

N = int(input())
F = [1, 1] + [0] * 50

for i in range(2, 50):
    F[i] = F[i-1] + F[i-2]
print(F[N-1])