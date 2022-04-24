# ! 한수
N = int(input())
ans = 0

for n in range(1, N+1):
    x = list(str(n))
    l = len(list(str(n)))
    for i in range(l-2):
        if int(x[i+2]) - int(x[i+1]) != int(x[i+1]) - int(x[i]):
            break
    else:
        ans += 1
print(ans)