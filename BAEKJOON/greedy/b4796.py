tc = 0
while True:
    tc += 1
    L, P, V = map(int, input().split())
    if not L and not P and not V: # 0 0 0 입력시 끝
        break
    quo, res = V//P, V%P # 몫, 나머지
    if res > L: # 남은 날이 L 보다 크면 L만큼 앞에서 꽉 채운다
        print('Case {}: {}'.format(tc, quo * L + L))
    else: # 남은 날이 L 보다 작으면 res만큼 꽉 채운다
        print('Case {}: {}'.format(tc, quo * L + res))