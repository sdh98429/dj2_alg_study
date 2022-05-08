# 그룹 단어 체커

N = int(input())
ans = 0

for _ in range(N):
    W = []
    S = input()
    for s in S:
        if s in W and s != W[-1]:
            break
        elif s not in W:
            W.append(s)
    else:
        ans += 1

print(ans)