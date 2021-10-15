# queue 풍선 터뜨리기
# 큐를 활용 못하고 해결, 다른 사람 코드 참고하기
N = int(input())

paper = list(map(int, input().split()))

ind = 0
for _ in range(N-1):
    move = paper[ind]
    paper[ind] = 0
    print(ind+1, end=' ')
    while move:
        if move > 0:
            ind = (ind + 1) % N
            if paper[ind]:
                move -= 1
        else:
            ind = (ind - 1) % N
            if paper[ind]:
                move += 1
print(ind+1)



