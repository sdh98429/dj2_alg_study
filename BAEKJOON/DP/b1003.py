# ! 피보나치 함수

T = int(input())

DP = [[1, 0],[0,1]] + [[] for _ in range(50)]

for i in range(2, 52):
    DP[i] = [DP[i-1][0] + DP[i-2][0], DP[i-1][1] + DP[i-2][1]]

for tc in range(1, T+1):
    N = int(input())
    print(*DP[N])