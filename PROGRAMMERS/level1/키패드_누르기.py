# 67256
# 키패드 누르기

pad = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]

def solution(numbers, hand):
    l = [3, 0]
    r = [3, 2]
    answer = []
    for n in numbers:
        for i in range(4):
            for j in range(3):
                if n == pad[i][j]:
                    if n in (1, 4, 7):
                        l[0], l[1] = i, j
                        answer += 'L'
                        break

                    if n in (3, 6, 9):
                        r[0], r[1] = i, j
                        answer += 'R'
                        break

                    ld = abs(l[0] - i) + abs(l[1] - j)
                    rd = abs(r[0] - i) + abs(r[1] - j)
                    if ld > rd:
                        r[0], r[1] = i, j
                        answer += 'R'
                    elif ld < rd:
                        l[0], l[1] = i, j
                        answer += 'L'
                    else:
                        if hand == 'right':
                            r[0], r[1] = i, j
                            answer += 'R'
                        else:
                            l[0], l[1] = i, j
                            answer += 'L'
                    break

    return ''.join(answer)

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))