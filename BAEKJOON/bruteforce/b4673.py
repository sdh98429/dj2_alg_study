# ! 셀프 넘버

S = [False] * (10001)

for i in range(1, 10001):
    if not S[i]: # 셀프 넘버일 수 있는 경우
        while i <= 10000: # 범위 안에 있으면
            i = i + sum(map(int, list(str(i)))) # 새롭게 다음 수
            if i <= 10000 and not S[i]: # 범위 안에 있고 아직 셀프넘버 아니다란 체크 안되어있으면
                S[i] = True

for i in range(1, 10001):
    if not S[i]:
        print(i)
