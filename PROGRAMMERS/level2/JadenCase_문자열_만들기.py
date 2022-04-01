# ! JadenCase 문자열 만들기
# 12951

def solution(s):
    answer = ''
    up = True # 대문자 변환할지 여부
    for w in s:
        if w != ' ': # 공백이 아니라면
            if up: # 대문자 처리
                answer = answer + w.upper()
            else: # 대문자 처리 X
                answer = answer + w.lower()
            up = False # 앞에 글자가 있으니 대문자 처리 X
        else: # 공백이라면 (' ' 자체 논리값은 True)
            answer = answer + ' ' # 공백 추가
            up = True # 다음 글자 대문자
    return answer

# s	return
# "3people unFollowed me"	"3people Unfollowed Me"
# "for the last week"	"For The Last Week"