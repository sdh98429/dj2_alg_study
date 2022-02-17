# 문자열 내 p와 y의 개수
# 12916

def solution(s):
    d = 0
    for r in s:
        if r in ('p', 'P'):
            d += 1
        if r in ('y', 'Y'):
            d -= 1

    return True if not d else False

# s	answer
# "pPoooyY"	true
# "Pyy"	false