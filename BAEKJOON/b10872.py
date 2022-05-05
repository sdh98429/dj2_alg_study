# 팩토리얼

N = int(input())

ans = 1
for i in range(1, N+1):
    ans *= i
print(ans)