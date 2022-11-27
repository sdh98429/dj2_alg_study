N, M, K = map(int, input().split())
team = min(N//2, M)
print(min(team, (N+M-K)//3))