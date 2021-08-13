N = int(input())

wgts = [int(input()) for _ in range(N)]

wgts.sort()
#버블 소트는 너무 오래 걸림
# for i in range(N-1, 0, -1):
#     for j in range(i):
#         if wgts[j] > wgts[j+1]:
#             wgts[j], wgts[j+1] = wgts[j+1], wgts[j]

max_w = 0
for i in range(N):
    if max_w < wgts[i] * (N-i):
        max_w = wgts[i] * (N-i)

print(max_w)