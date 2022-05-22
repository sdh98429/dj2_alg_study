# 단어 공부

S = list(input())

A = [0] * 26
for s in S:
    if ord(s) >= 97:
        A[ord(s)-97] += 1
    else:
        A[ord(s)-65] += 1

max_a = 0
ans = '?'
for i in range(len(A)):
    if A[i] > max_a:
        max_a = A[i]
        ans = chr(i+65)
    elif A[i] == max_a:
        ans = '?'
print(ans)
