# 로또의 최고 순위와 최저 순위

def solution(lottos, win_nums):
    cons = 0
    vari = 0
    for lot in lottos:
        if lot in win_nums:
            cons += 1
        elif not lot:
            vari += 1
    answer = [7-cons-vari if cons+vari>1 else 6, 7-cons if cons > 1 else 6]
    return answer

print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]))
print(solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]))