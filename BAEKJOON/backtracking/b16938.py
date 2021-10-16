# backtracking 캠프 준비
# 아래는 가지치기 하려했지만 실패
# 완전탐색으로 해결

# def backtrack(ind, num, min_l, max_l, tot):
#     global cnt
#     if ind == N:
#         if num >= 2 and max_l - min_l >= X and R >= tot >= L:
#             cnt +=1
#         return
#
#     backtrack(ind+1, num, min_l, max_l, tot)
#     min_l = min(A[ind], min_l)
#     max_l = max(A[ind], max_l)
#     if num == 0:
#         backtrack(ind+1, num + 1, min_l, max_l, tot + A[ind])
#     else:
#         if max_l - min_l >= X and tot + A[ind] <= R:
#             backtrack(ind+1, num+1, min_l, max_l, tot + A[ind])

def backtrack(ind, num, min_l, max_l, tot):
    global cnt
    if ind == N:
        if num >= 2 and max_l - min_l >= X and L <= tot <= R:
            cnt += 1
        return
    backtrack(ind+1, num, min_l, max_l, tot)
    min_l = min(A[ind], min_l)
    max_l = max(A[ind], max_l)
    backtrack(ind+1, num+1, min_l, max_l, tot + A[ind])

N, L, R, X = map(int, input().split())
A = list(map(int, input().split()))
cnt = 0
backtrack(0, 0, 9987654321, 0, 0)
print(cnt)