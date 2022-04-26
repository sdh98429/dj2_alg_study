# !! 1로 만들기, dfs는 RecursionError이므로 큐 사용

# N = int(input())
# D = [123456789] * (N+1)
# D[N] = 0
# def act(n):
#     global D
#     if n <= 1:
#         return
#     if not n%3:
#         if D[n//3] > D[n] + 1:
#             D[n//3] = D[n] + 1
#             act(n//3)
#     if not n%2:
#         if D[n//2] > D[n] + 1:
#             D[n//2] = D[n] + 1
#             act(n//2)
#     if D[n-1] > D[n] + 1:
#         D[n-1] = D[n] + 1
#         act(n-1)
    
# act(N)

# print(D[1])

N = int(input())
Q = [N]
D = [False] * (N+1)
# D[N] = 0
ans = 0
flag = True
while flag:
    NQ = []
    for q in Q:
        if q == 1:
            print(ans)
            flag = False
            break
        if not q%3:
            if not D[q//3]:
                D[q//3] = True
                NQ.append(q//3)
        if not q%2:
            if not D[q//2]:
                D[q//2] = True
                NQ.append(q//2)
        if not D[q-1]:
            D[q-1] = True
            NQ.append(q-1)
    Q = NQ
    ans += 1

