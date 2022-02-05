# ! 멀쩡한 사각형, 최대공약수
# 62048

def solution(w, h):
    if w > h:  # 작은 쪽을 w로 맞춰줍니다
        w, h = h, w
    div = 1  # w, h의 최대 공약수
    for i in range(1, int(w ** 1 / 2) + 1):  # 작은 수의 제곱근까지 약수 탐색
        if not w % i:  # i가 w의 약수면
            if not h % i:  # h의 약수이면
                if i > div:  # 최대인지 확인
                    div = i
            if not h % (w // i):  # w//i가 h의 약수이면
                if w // i > div:  # 최대인지 확인
                    div = w // i

    return w * h - (div) * ((w + h) // div - 1)  # 최대 공약수만큼 (가로, 세로) 조각을 나눕니다. 서로소 w//div, h//div 의 합-1만큼 절취선이 지나갑니다.

# W	H	result
# 8	12	80