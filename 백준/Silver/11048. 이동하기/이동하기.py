
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

maze = [list(map(int, input().split())) for _ in range(N)]
DP = [[0]*M for _ in range(N)]
DP[0][0] = maze[0][0]

for i in range(N):
  for j in range(M):
    DP[i][j] = max(DP[i-1][j]+maze[i][j] if i > 0 else maze[i][j], DP[i][j-1]+maze[i][j] if j > 0 else maze[i][j])

print(DP[N-1][M-1])