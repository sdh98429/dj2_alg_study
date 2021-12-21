M = list(input())
K = list(input())

alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

table = [[0] * 5 for _ in range(5)]

ind = 0
used = []
for k in K:
    if not k in used:
        table[ind//5][ind%5] = k
        used.append(k)
        ind += 1

for a in alpha:
    if a not in used:
        table[ind//5][ind%5] = a
        ind += 1

pair = []
i = 0
while i < len(M):
    if i+1 < len(M):
        if M[i] != M[i+1]:
            pair += [M[i] + M[i+1]]
            i += 2
        else:
            if M[i] != 'X':
                pair += [M[i] + 'X']
            else:
                pair += [M[i] + 'Q']
            i += 1
    else:
        pair += [M[i] + 'X']
        i += 1


ans = ''
for pa in pair:
    loc = []
    for p in list(pa):
        for i in range(5):
            for j in range(5):
                if table[i][j] == p:
                    loc.append((i,j))
    else:
        if loc[0][0] == loc[1][0]:
            ans += table[loc[0][0]][(loc[0][1]+1)%5]
            ans += table[loc[1][0]][(loc[1][1] + 1) % 5]
        elif loc[0][1] == loc[1][1]:
            ans += table[(loc[0][0]+1)%5][loc[0][1]]
            ans += table[(loc[1][0]+1)%5][loc[1][1]]
        else:
            ans += table[loc[0][0]][loc[1][1]]
            ans += table[loc[1][0]][loc[0][1]]

print(ans)