# 알파벳 찾기

S = input()
ALP = [-1] * 26
for i in range(len(S)):
    if ALP[ord(S[i])-97] == -1:
        ALP[ord(S[i])-97] = i
print(*ALP)
