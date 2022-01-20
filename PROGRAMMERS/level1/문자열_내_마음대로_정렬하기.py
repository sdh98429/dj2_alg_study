# 문자열 내 마음대로 정렬하기
# 12915

def solution(strings, n):
    words = []
    answer = []
    strings.sort()
    for i in range(len(strings)):
        words.append((strings[i][n], i))

    words.sort()
    for w in words:
        answer.append(strings[w[1]])

    return answer

# strings	n	return
# ["sun", "bed", "car"]	1	["car", "bed", "sun"]
# ["abce", "abcd", "cdx"]	2	["abcd", "abce", "cdx"]