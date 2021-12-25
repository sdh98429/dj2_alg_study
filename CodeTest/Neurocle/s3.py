# 실패
# 우선순위큐와 힙을 이용해야 할 듯

N, M = map(int, input().split())
# used = [0] * N
# parent = [[] for _ in range(N)]

word = [i for i in range(N)]


for _ in range(M):
    pair = list(input())
    s = -1
    e = -1
    for i in range(N):
        if word[i] == ord(pair[0])-65:
            s = i
        if word[i] == ord(pair[1])-65:
            print(i, word[i])
            e = i
    if s > e:
        word[s] = int(word[e])
        word[e] = int(word[s])
    print(s,e, word)


    # if word[ord(pair[0])-65] > word[ord(pair[1])-65]:
    #     word[ord(pair[0]) - 65], word[ord(pair[1])-65] = word[ord(pair[1]) - 65], word[ord(pair[0])-65]
    # print(word)
    # used[ord(pair[0]-65)] = 1
    # used[ord(pair[1] - 65)] = 1

print(word)
# for i in range(N):
#     if not used[i]:
