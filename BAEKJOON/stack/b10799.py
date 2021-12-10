# stack ! 쇠막대기
# SSAFY에서 예전에 한 번 풀었던 문제


STEEL = list(input())

# 스택 크기
top = 0
# 직전에 이미 한 번 잘랐는지 확인
cut = False
ans = 0 # 조각 수
for s in STEEL:
    if s == '(':
       top += 1
       cut = False # 직전에 자르지 않았단 처리
    else:
        top -= 1
        if cut: # 직전에 한 번 잘랐다면 한 조각만 추가
            ans += 1
        else: # 처음 자르는 거면 스택 크기 만큼 추가
            ans += top
        cut = True

print(ans)