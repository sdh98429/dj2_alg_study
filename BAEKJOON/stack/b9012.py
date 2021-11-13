# stack 괄호
# ()가 개수 다르면 NO
# 과정 중 )가 (보다 더 많으면 NO

T = int(input())

for tc in range(T):
    word = list(input())
    cnt = 0
    flag = 0
    for w in word:
        if cnt < 0:
            break
        if w == '(':
            cnt += 1
        else:
            cnt -= 1
    else:
        if not cnt:
            print('YES')
            continue
    print('NO')

