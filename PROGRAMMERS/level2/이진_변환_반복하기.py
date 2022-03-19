# ! 이진 변환 반복하기, bin 사용
# 70129

def solution(string):
    zero = 0 # 제거한 0의 수
    change = 0 # 시행 횟수
    while string != '1':
        change += 1 # 시행 추가
        one = 0 # 1의 개수
        for s in string:
            if s == '0':
                zero += 1
            else:
                one += 1
        string = bin(one)[2:] # 파이썬 내장함수로 이진수 십진수로 변환, 앞의 0b 제거
    return [change, zero]

# s	result
# "110010101001"	[3,8]
# "01110"	[3,3]
# "1111111"	[4,1]

