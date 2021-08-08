import copy
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

# while not score == sum(sum(mat,[])):

#     score = sum(sum(mat,[]))
#     score_r = 0
#     score_c = 0
#     for i in range(T):
#         if 3-sum(mat[i]) < sum(mat[i]):
#             score_r += (2 * sum(mat[i]) - 3)

#     for j in range(T):
#         if 3-sum(mat[:][j]) < sum(mat[:][j]):
#             score_c += (2 * sum(mat[:][j]) - 3)
#     print(score_r, score_c)
#     if not (score_r + score_c):
#         break
#     elif score_r > score_c:
#         for i in range(T):
#             if 3-sum(mat[i]) < sum(mat[i]):
#                 for s in range(T):
#                     mat[i][s] = 1 - mat[i][s]
#     else:
#         for j in range(T):
#             if 3-sum(mat[:][j]) < sum(mat[:][j]):
#                 for s in range(T):
#                     mat[s][j] = 1 - mat[s][j]



score = sum(sum(mat,[]))
score_r = 0
score_c = 0
for i in range(T):
    if 3-sum(mat[i]) < sum(mat[i]):
        score_r += (2 * sum(mat[i]) - 3)

for j in range(T):
    print(mat)
    # print(sum(mat[:][j]))
    
    if 3-sum(m[j] for m in mat) < sum(m[j] for m in mat):
        score_c += (2 * sum(m[j] for m in mat) - 3)
print(score_r, score_c)
# if not (score_r + score_c):
#     break
# elif score_r > score_c:
#     for i in range(T):
#         if 3-sum(mat[i]) < sum(mat[i]):
#             for s in range(T):
#                 mat[i][s] = 1 - mat[i][s]
# else:
#     for j in range(T):
#         if 3-sum(mat[:][j]) < sum(mat[:][j]):
#             for s in range(T):
#                 mat[s][j] = 1 - mat[s][j]

print(score)