# ! 이상한 문자 만들기, 공백 문자열 True
# 12930

def solution(s):
    i = 0 # 각 단어에 해당하는 인덱스
    answer = ''
    for ind in range(len(s)):
        if s[ind].strip(): # s[ind]로만 하면 ' ' 공백 입력시 type string으로 True가 나옴
            if not i%2:
                answer = answer + s[ind].upper()
            else:
                answer = answer + s[ind].lower()
            i += 1
        else:
            answer = answer + ' '
            i = 0 # 각 단어 인덱스 초기화
    return answer

# print(solution('don  acssdf  aafs'))
# 97 122 a
# 65 90 A

# s	return
# "try hello world"	"TrY HeLlO WoRlD"