N = int(input())
L = list(map(int, input().split()))
m = int(input())
tot = 0
for l in L:
    if l == m:
        tot += 1
print(tot)