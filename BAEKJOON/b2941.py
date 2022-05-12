# 크로아티아 알파벳

S = list(input())

C = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

i = 0
ans = 0
while i < len(S):
    ans += 1
    if ''.join(S[i:i+2]) in C:
        i += 2
    elif ''.join(S[i:i+3]) in C:
        i += 3
    else:
        i+= 1
print(ans)

