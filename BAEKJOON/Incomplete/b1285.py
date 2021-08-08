import copy
T = int(input())
mat = list()
for i in range(T):
    mat.append([])
    # for s in range(T):
    #     mat[i].append(0)
for i in range(T):
    str_row = list(input())
    for j in range(T):
        if str_row[j] == "T":
            mat[i].insert(j, 1)
        else:
            mat[i].insert(j, 0)
# print(mat)
# print(sum(sum(mat,[])))
score = 0
# print(sum(mat[:][2]))
while not score == sum(sum(mat,[])):
    # print(mat)
    # mat_r = copy.deepcopy(mat)
    # mat_c = copy.deepcopy(mat)
    score = sum(sum(mat,[]))
    score_r = 0
    score_c = 0
    for i in range(T):
        if 3-sum(mat[i]) < sum(mat[i]):
            # for s in range(T):
            #     mat_r[i][s] = 1 - mat_r[i][s]
            score_r += (2 * sum(mat[i]) - 3)

    for j in range(T):
        if 3-sum(m[j] for m in mat) < sum(m[j] for m in mat):
            # for s in range(T):
            #     mat_c[s][j] = 1 - mat_c[s][j]
            score_c += (2 * sum(m[j] for m in mat) - 3)
    # print(score_r, score_c)
    if not (score_r + score_c):
        break
    elif score_r > score_c:
        for i in range(T):
            if 3-sum(mat[i]) < sum(mat[i]):
                for s in range(T):
                    mat[i][s] = 1 - mat[i][s]
    else:
        for j in range(T):
            if 3-sum(m[j] for m in mat) < sum(m[j] for m in mat):
                for s in range(T):
                    mat[s][j] = 1 - mat[s][j]
    # if sum(sum(mat_r,[])) < sum(sum(mat_c,[])):
    #     mat =copy.deepcopy(mat_r)
    # else:
    #     mat =copy.deepcopy(mat_c)

print(score)