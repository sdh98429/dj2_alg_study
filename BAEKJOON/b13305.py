N = int(input())
dists = list(map(int,input().split()))
pris = list(map(int,input().split()))[:-1]


result = term = 0
profit = pris[0]
for i in range(N-1):
    if pris[i] < profit:
        result += term * profit
        term = 0
        profit = pris[i]
    term += dists[i]
result += term * profit
print(result)
