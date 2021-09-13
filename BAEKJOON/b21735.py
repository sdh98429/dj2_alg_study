
def roll(time = 0, i = -1, size = 1):
    global max_size

    if time == M or i == N-1:
        if size > max_size:
            max_size = size
        return

    roll(time+1, i+1, size + A[i+1])
    
    if i+2 < N:
        roll(time+1, i+2, size//2 + A[i+2])

N, M = list(map(int, input().split()))
A = list(map(int, input().split()))
max_size = 0
roll()
print(max_size)















# print(A)
# li = [[-1, 1]]
# li = [1, 1+A[1]]
# time = []
# for i in range(1, N):
#     for vol in 


# #     if li[i-1][1]//2 + A[li[i-1][0]+2] >= li[i-1][1] + A[li[i-1][0]+1]:
# #         li.append([li[i-1][0]+2, li[i-1][1]//2 + A[li[i-1][0]+2]])
# #     else:
# #         li.append([li[i-1][0]+1, li[i-1][1] + A[li[i-1][0]+1]])
# # print(li)