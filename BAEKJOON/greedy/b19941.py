# greedy 햄버거
# 사람이 있는 곳 기준으로 거리 K만큼 왼쪽부터 오른쪽까지 조사
# 만약 햄버거가 있다면 먹은 처리 해줌

N, K = map(int, input().split())
LINE = list(input())
line = [0] * N # 안먹은 햄버거 0, 사람 1, 먹은 햄버거 2
for i in range(N):
    if LINE[i] == 'P':
        line[i] = 1 # 사람

cnt = 0 # 먹은 개수
for i in range(N): # 모든 요소에 대해
    if line[i] == 1: # 만약 사람이라면
        for k in range(-K, K+1): # 왼쪽부터 먹는게 이득이니 왼쪽부터 조사
            if i+k in range(N) and line[i+k] == 0: # 범위 안에 있고, 안 먹은 햄버거면
                line[i+k] = 2 # 햄버거 먹은 처리
                cnt += 1 # 먹은 개수 늘리고
                break # 다음 사람 찾으러 간다

print(cnt)