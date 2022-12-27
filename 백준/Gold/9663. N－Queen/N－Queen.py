from collections import deque

def Back(ni):
  global tot # 방법의 수
  if ni >= N: # 마지막 행까지 도달
    tot += 1
    return
  
  for nj in range(N): # 퀸을 놓는 위치 ni, nj
    if J[nj] != 1: # nj열에 퀸이 없다면
      flag = True # 놓을 수 있는 지 여부
      for b in B: # 기존의 퀸들과 확인
        if flag:
          bi, bj = b # 기존의 퀸들의 위치
          if ni == bi or nj == bj or abs(ni - bi) == abs(nj - bj): # 가로, 세로, 대각선 체크
            flag = False
      if flag: # 안 겹친다면 현재 위치 추가해서 재귀
        B.append([ni, nj])
        J[nj] = 1
        # I[nj] = 1
        Back(ni+1)
        B.pop()
        J[nj] = 0
        # I[nj] = 0
                       
N = int(input())
tot = 0

B = deque()
J = [0] * N # 퀸이 이미 있는 열 체크
# I = [0] * N # 퀸이 이미 있는 행 체크
Back(0)
print(tot)