N, K = list(map(int,input().split()))

money = [0] * N
for i in range(N):
    money[i] = int(input())

result = 0
for j in range(N-1,-1,-1):
    if money[j] > K:
        continue
    else:
        result += K//money[j]
        K = K%money[j]
    if not money[j]:
        break
print(result) 