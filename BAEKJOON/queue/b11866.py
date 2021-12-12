# queue 요세푸스 문제 0
# 1~N 까지의 숫자를 큐에 넣고
# K 번이 아닐 떄는 빼고 넣고를 반복,
# K 번일 때는 빼기만 하기


from collections import deque

N, K = map(int, input().split())

q = deque()
for n in range(1, N+1):
    q.append(n)

print("<", end="")
k = 0
while q:
    v = q.popleft()
    k = (k+1)%K
    if k == 0:
        if q:
            print(v, end=", ")
        else:
            print(v, end=">")
    else:
        q.append(v)

# 시간 초과
# N, K = map(int, input().split())
#
# visited = [0] * N
# k = 0
# ind = -1
#
# print("<", end="")
# while sum(visited) < N:
#     ind = (ind + 1)%N
#
#     if not visited[ind]:
#         k += 1
#
#     if k == K:
#         visited[ind] = 1
#         if sum(visited) == N:
#             print(ind+1, end=">")
#         else:
#             print(ind+1, end=", ")
#         k = 0





