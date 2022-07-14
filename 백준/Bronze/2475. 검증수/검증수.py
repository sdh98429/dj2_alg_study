S = list(map(int, input().split()))
tot = 0
for s in S:
    tot += s ** 2
print(tot%10)