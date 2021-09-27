import sys
input = sys.stdin.readline
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    score1 = [0] * N
    score2 = [0] * N
    score = [0] * N
    dp = [0] * N
    for i in range(N):
        score1[i], score2[i] = map(int, input().split())
        score[score1[i]-1] = score2[i]

    dp[0] = score[0]
    max_worker = 0
    for i in range(1, N):
        if score[i] < dp[max_worker]:
            max_worker += 1
            dp[max_worker] = score[i]

    print(max_worker+1)