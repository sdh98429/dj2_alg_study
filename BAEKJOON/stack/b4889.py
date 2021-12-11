# stack 안정적인 문자열
# stack이 0 보다 작아지면 닫힌 괄호를 열린 괄호로 바꿈
# 최종 stack이 0 보다 크면 top의 절반만큼 열린 괄호를 닫힌 괄호로 바꿔줌

tc = 0 # 테스트 케이스
while True:
    tc += 1
    W = list(input())
    if W[0] == '-': # 종결 조건 확인
        break
    top = 0 # 스택 크기
    ans = 0 # 변경 수
    for w in W:
        if w == '{':
            top += 1
        else:
            top -= 1
        if top < 0: # 닫힌 괄호 열린 괄호로 변경
            top += 2
            ans += 1
    if top != 0: # 최종적으로 0 아닐 시 열린 괄호 닫힌 괄호로 변경
        ans += int(top/2)
    print("{0}. {1}".format(tc, ans))