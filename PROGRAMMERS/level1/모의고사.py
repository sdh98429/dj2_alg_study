# 모의고사
# 42840

def solution(answers):
    answer = []
    p = [0, 0, 0]
    a2 = [1, 3, 4, 5]
    a3 = [3, 1, 2, 4, 5]
    for i in range(len(answers)):
        if i % 5 + 1 == answers[i]:
            p[0] += 1
        if (not i % 2 and answers[i] == 2) or (i % 2 and answers[i] == a2[(i // 2) % 4]):
            p[1] += 1
        if answers[i] == a3[(i // 2) % 5]:
            p[2] += 1

    for i in range(3):
        if p[i] == max(p):
            answer.append(i + 1)

    return answer

# answers	return
# [1,2,3,4,5]	[1]
# [1,3,2,4,2]	[1,2,3]