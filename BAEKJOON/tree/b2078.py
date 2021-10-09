L, R = map(int, input().split())
# 역순으로 타고 오른다
a = b = 0
while True:
    if L == 1: # L이 먼저 1이 된 경우 우측에 R-1번만큼 나누고 끝난다
        b += R - 1
        break
    elif R == 1: # R이 먼저 1이 된 경우 좌측에 L-1번만큼 나누고 끝난다
        a += L - 1
        break
    if L > R:
        a += L//R # L을 R로 나눌 수 있는 만큼 좌측에 더해줌
        L %= R # L을 R로 나눈 나머지 만큼 L이 남음
    else:
        b += R//L
        R %= L

print(a, b)