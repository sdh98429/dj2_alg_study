# stack 원숭이 매달기
# 각 덩굴에 몇 마리 매달린지 맞춰야 하는줄 알았는데 아니었음

N = int(input())

for _ in range(N):
    max_cnt = 0
    cnt = 0
    words = list(input())
    for w in words:
        if w == '[':
            cnt += 1
        else:
            cnt -= 1
        if cnt > max_cnt:
            max_cnt = cnt
    print( 2 ** max_cnt)