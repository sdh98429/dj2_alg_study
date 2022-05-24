# 최댓값

big = 0
ind = 0
for i in range(1, 10):
    n = int(input())
    if n > big:
        big = n
        ind = i
print(big)
print(ind)