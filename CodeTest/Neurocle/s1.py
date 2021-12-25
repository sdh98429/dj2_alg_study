
X, N = map(int, input().split())

ans = ''
while X:
    res = X % N
    if N > 10 and res >= 10:
        ans = chr(res+55) + ans
    else:
        ans = str(res) + ans
    X //= N

print(ans)