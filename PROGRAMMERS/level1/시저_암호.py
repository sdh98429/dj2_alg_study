# 시저 암호
# 12926

def solution(s, n):
    answer = ''
    for a in s:
        if 65 <= ord(a) <= 90:
            answer += chr(65 +(ord(a) + n -65) %26)
        elif 97 <= ord(a) <= 122:
            answer += chr(97 +(ord(a) + n -97) %26)
        else:
            answer += ' '
    return answer

# 97 122
# 65 90
# 32

# s	n	result
# "AB"	1	"BC"
# "z"	1	"a"
# "a B z"	4	"e F d"