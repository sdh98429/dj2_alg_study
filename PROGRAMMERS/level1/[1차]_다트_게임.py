# [1차] 다트 게임
# 17682

def solution(dartResult):
    sc = []  # 각 점수
    ten = False  # 10인지 확인
    for d in list(dartResult):
        if ord(d) in range(48, 58):  # 숫자라면
            if ten:  # 전에도 숫자라면 10
                sc[-1] = 10
            else:  # 전에 숫자 아니라면 한자리수
                sc.append(int(d))
                ten = True
            continue
        ten = False
        if d == 'D':
            sc[-1] = sc[-1] ** 2
        if d == 'T':
            sc[-1] = sc[-1] ** 3
        if d == '*':
            sc[-1] *= 2
            if len(sc) > 1:  # 만약 길이가 1 초과면 전에 점수 고려
                sc[-2] *= 2
        if d == '#':
            sc[-1] = -sc[-1]

    return sum(sc)

# 예제	dartResult	answer	설명
# 1	1S2D*3T	37	11 * 2 + 22 * 2 + 33
# 2	1D2S#10S	9	12 + 21 * (-1) + 101
# 3	1D2S0T	3	12 + 21 + 03
# 4	1S*2T*3S	23	11 * 2 * 2 + 23 * 2 + 31
# 5	1D#2S*3S	5	12 * (-1) * 2 + 21 * 2 + 31
# 6	1T2D3D#	-4	13 + 22 + 32 * (-1)
# 7	1D2S3T*	59	12 + 21 * 2 + 33 * 2