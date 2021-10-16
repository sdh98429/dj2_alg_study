# 근손실
# 조합으로 해결
# 중간 중간에 tot이 0보다 작아지면 가지치기를 해줘야한다.

def backtrack(ind, tot):
    global cnt

    if tot < 0:
        return

    if ind == N:
        cnt += 1
        return

    for i in range(N):
        if not used[i]:
            used[i] = 1
            backtrack(ind+1, tot + A[i] - K) # K에 4라는 상수 넣었다 틀림
            used[i] = 0

N, K = map(int, input().split())
A = list(map(int, input().split()))
used = [False] * (N+1)
cnt = 0
backtrack(0, 0)
print(cnt)