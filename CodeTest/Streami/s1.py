# Example test:   'aabbb'
# OK
#
# Example test:   'ba'
# OK
#
# Example test:   'aaa'
# OK
#
# Example test:   'b'
# OK
#
# Example test:   'abba'
# OK

def solution(S):
    W = list(S)
    flag = False
    ans = True
    for w in W:
        if w == 'b' and not flag:
            flag = True
        if w == 'a' and flag:
            ans = False
            break
    return ans

print(solution('abab'))