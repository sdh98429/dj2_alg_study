# 도서관
# 0 기준으로 왼쪽 끝에서부터 M개, 오른쪽 끝에서 M개씩 모은다
# 왼쪽 끝과 오른쪽 끝 중 더 큰 절대값을 가진 쪽을 도착점으로 한다
N, M = map(int, input().split())
B = list(map(int, input().split()))
# 거리 순 정렬
B.sort()

tot = 0 # 총합
for i in range(len(B)):
    # 왼쪽에 있다면
    if B[i] < 0:
        # M개의 그룹 중 가장 큰 절대값은 맨 왼쪽에 위치
        if not i%M:
            # 왕복
            tot += - 2 * B[i]
    else:
        break

for j in range(len(B)):
    # 오른쪽에 있다면
    if B[::-1][j] > 0:
        # M개의 그룹 중 가장 큰 절대값은 맨 오른쪽에 위치
        if not j%M:
            # 왕복
            tot += 2 * B[::-1][j]
    else:
        break

# 가장 큰 절대값은 도착점이므로 왕복 안해도 됨
tot -= max(abs(B[0]), abs(B[-1]))

print(tot)


