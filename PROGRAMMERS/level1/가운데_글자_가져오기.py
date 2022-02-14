# 가운데 글자 가져오기
# 12903

def solution(s):
    return s[len(s)//2] if len(s)%2 else s[len(s)//2-1:len(s)//2+1]

# s	return
# "abcde"	"c"
# "qwer"	"we"