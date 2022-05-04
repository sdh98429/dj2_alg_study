# 스티커 ! 한 줄 아무것도 안 고른 경우

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    U = list(map(int, input().split())) # 위의 스티커들
    D = list(map(int, input().split())) # 아래의 스티커들
    before = [U[0], D[0], 0] # 전에 위의 스티커를 고른 경우, 아래 스티커를 고른 경우, 아예 고르지 않은 경우의 최대값

    for i in range(1, N):
        after = [max(U[i]+before[1], U[i]+before[2]), max(D[i]+before[0], D[i]+before[2]), max(before[0], before[1])] # (위 고른 경우 = 직전에 아래 고르거나 아무것도 안 고르거나, 아래 = 직전 위 or 아무것도, 아무것도 안 고른 경우= 직전 최대값)
        before = after.copy() # 직전 결과 가져오기
    print(max(before))