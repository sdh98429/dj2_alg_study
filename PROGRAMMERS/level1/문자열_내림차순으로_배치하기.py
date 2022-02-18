# 문자열 내림차순으로 배치하기
# 12917

def solution(s):
    answer = []
    for r in s:
        answer.append(r)
    answer.sort(reverse=True)
    return ''.join(answer)

# s	return
# "Zbcdefg"	"gfedcbZ"