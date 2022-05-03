# 이친수

N = int(input())

one = [1] + [0] * (N-1)
zero = [0] * (N)

for i in range(1, N):
    one[i] = zero[i-1]
    zero[i] = zero[i-1] + one[i-1]

print(one[N-1] + zero[N-1])