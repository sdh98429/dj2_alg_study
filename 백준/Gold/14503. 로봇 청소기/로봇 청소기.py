from collections import deque
dr = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def BFS(r, c, d):
  tot = 0 # 청소 구역 개수
  q = deque()
  q.append([r, c, d])
  while q:
    vr, vc, vd = q.popleft()
    if not maze[vr][vc]: # 청소하기
      maze[vr][vc] = 2
      tot += 1
    for i in range(1, 5):
      drr, drc = dr[(vd - i)%4] # 현재 방향 시작, 반시계 방향 회전
      wr, wc = drr + vr, drc + vc
      if wr in range(N) and wc in range(M) and not maze[wr][wc]: # 빈 공간이면 이동 후 다시 시작
        q.append([wr, wc, (vd - i)%4])
        break
    else: # 4방향 모두 청소 불가
      wr, wc = vr - dr[vd][0], vc - dr[vd][1]
      if wr in range(N) and wc in range(M) and maze[wr][wc] != 1: # 후진 가능
        q.append([wr, wc, vd])
      else: # 후진 불가
        return tot
      
  
N, M = map(int, input().split())
r, c, d = map(int, input().split())

maze = [list(map(int, input().split())) for _ in range(N)]
print(BFS(r, c, d))
