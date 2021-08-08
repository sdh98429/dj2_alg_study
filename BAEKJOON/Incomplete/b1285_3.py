T = int(input())
mat = list()
for i in range(T):
    mat.append([])

for i in range(T):
    str_row = list(input())
    for j in range(T):
        if str_row[j] == "T":
            mat[i].insert(j, 1)
        else:
            mat[i].insert(j, 0)


score = 0
while not score == sum(sum(mat,[])):
    tot_r = 0
    tot_c = 0
    # print('one')
    score = sum(sum(mat,[]))

    for i in range(T):
        if sum(mat[i]) > T - sum(mat[i]):
            tot_r += T - sum(mat[i])
        else:
            tot_r += sum(mat[i])

    for j in range(T):
        if sum(m[j] for m in mat) > T - sum(m[j] for m in mat):
            tot_c += T - sum(m[j] for m in mat)
        else:
            tot_c += sum(m[j] for m in mat)
    # print(tot_r, tot_c)
    if min(tot_r, tot_c) >= score:
        break
    elif tot_r < tot_c:
        for i in range(T):
            if sum(mat[i]) > T - sum(mat[i]):
                for s in range(T):
                    mat[i][s] = 1 - mat[i][s]

    else:
        for j in range(T):
            if sum(m[j] for m in mat) > T - sum(m[j] for m in mat):
                for s in range(T):
                    mat[s][j] = 1 - mat[s][j]

print(score)
# print(tot_r, tot_c)
