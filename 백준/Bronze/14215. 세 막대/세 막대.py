L = sorted(list(map(int, input().split())))
print(2*(L[0] + L[1])-1 if (L[0] + L[1] <= L[2]) else sum(L))