
N = int(input())

L = []
for _ in range(N):
  L.append(list(map(int, input().split())))

DP_min = L[0][:]
DP_max = L[0][:]


for i in range(1, N):
  tmp_min = DP_min[:]
  DP_min[0] = min(tmp_min[0] + L[i][0], tmp_min[1] + L[i][0])
  DP_min[1] = min(tmp_min[0] + L[i][1], tmp_min[1] + L[i][1], tmp_min[2] + L[i][1])
  DP_min[2] = min(tmp_min[1] + L[i][2], tmp_min[2] + L[i][2])


for i in range(1, N):
  tmp_max = DP_max[:]
  DP_max[0] = max(tmp_max[0] + L[i][0], tmp_max[1] + L[i][0])
  DP_max[1] = max(tmp_max[0] + L[i][1], tmp_max[1] + L[i][1], tmp_max[2] + L[i][1])
  DP_max[2] = max(tmp_max[1] + L[i][2], tmp_max[2] + L[i][2])

print(max(DP_max), min(DP_min))
