# 숫자의 개수
ans = 1
for _ in range(3):
    ans *= int(input())
ans = list(str(ans))

one = [0] * 10
for a in ans:
    one[int(a)] += 1

for o in one:
    print(o)
