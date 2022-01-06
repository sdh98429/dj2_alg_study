# 81301
# ! 숫자 문자열과 영단어
# dict에서 앞에 3글자만 찾기

N_d = {'zer' : (0,4), 'one' : (1,3), 'two' : (2,3), 'thr' : (3,5), 'fou' : (4,4), 'fiv' : (5,4), 'six' : (6,3), 'sev' : (7,5), 'eig' : (8,5), 'nin' : (9,4)}

def solution(s):
    answer = []
    let = list(s)
    ind = 0
    while ind < len(let):
        if ord(let[ind]) in range(48, 58):
            answer.append(let[ind])
            ind += 1
        else:
            num = ''.join(let[ind:ind+3])
            n = N_d.get(num)
            answer.append(str(n[0]))
            ind += n[1]


    return int(''.join(answer))

print(solution("one4seveneight"))
print(solution("23four5six7"))
print(solution("2three45sixseven"))
print(solution("123"))


# print(ord('1')) # 48 58
# one
# two
# three
# four
# five
# six
# seven
# eight
# nine
# ten