# 문자열 다루기 기본
# 12918

def solution(s):
    answer = False
    if len(s) in (4,6):
        try:
            int(s)
            answer = True
        except:
            pass
        
    return answer

# s	return
# "a234"	false
# "1234"	true