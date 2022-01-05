# 72410
# !! 신규 아이디 추천
# 조건이 많아 많이 헤맸음

def solution(new_id):
    new = []
    for n in list(new_id):
        if n in ('-', '_', '.' ) or ord(n) in range(97, 123) or ord(n) in range(48, 58):
            new.append(n)

        elif ord(n) in range(65, 91):
            new.append(chr(ord(n)+32))
    answer = []
    if new:
        flag = True
        end = 0
        for n in new:
            if end in range(15):
                if n == '.':
                    if flag and end:
                        answer.append(n)
                        end += 1
                        flag = False
                else:
                    flag = True
                    answer.append(n)
                    end += 1
        if end and answer[end-1] == '.':
            answer.pop()

        if not answer:
            answer = ['a']
    else:
        answer = ['a']

    t = len(answer) # len(answer) 쓰면 for에서 길이 바뀜
    if t < 3:
        for _ in range(3 - t):
            answer.append(answer[t-1])

    return ''.join(answer)



print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))
# print(chr(range(97, 123)))
# 97 122
# 65 90
# print(chr(97))
# print(ord('9'))

