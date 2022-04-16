# 더하기 사이클

N = input()
new = N
ans = 0
while True:
    ans += 1
    new = list(new)[-1] + list(str(sum(map(int, list(new)))))[-1]
    if int(new) == int(N):
        print(ans)
        break