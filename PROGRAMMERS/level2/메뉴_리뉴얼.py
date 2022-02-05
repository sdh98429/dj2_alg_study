# !! 메뉴 리뉴얼, 조합 라이브러리 사용
# 72411

from itertools import combinations


def solution(orders, course):
    answer = []

    for c in course:  # 이번 코스 메뉴 개수 c개
        cand = []  # 가능한 조합
        for ord in orders:  # orders 안 order에서 가능한 조합을 찾아 cand에 넣기 'ABC'에서 'AB' 'AC' 'BC' 찾기
            cand_o = list(combinations(sorted(list(ord)), c))  # 조합 합수 사용함, sorted는 XW를 WX 등 알파벳 순으로 바꿔줌
            for c_o in cand_o:
                if c_o not in cand:
                    cand.append(c_o)

        max_cnt = 2  # 가장 많이 주문된 조합 주문수, 최소 2명 이상에게 제공
        max_menu = []  # 가장 많이 주문된 조합 주문 종류
        for can in cand:  # 위의 가능한 조합에서 하나 택1
            now = 0  # 현재 조합 주문된 횟수
            for ord in orders:
                for c in can:
                    if not c in ord:  # 만약 현재 조합에서 이번 주문이 불가능 하면 break
                        break
                else:
                    now += 1  # 주문 가능
            if now == max_cnt:  # 최대 주문 수와 같으면 메뉴 추가
                max_menu.append(''.join(can))
            elif now > max_cnt:  # 최대 주문 수보다 많으면 메뉴 초기화하고 추가
                max_cnt = now
                max_menu = [''.join(can)]
        answer += max_menu

    return sorted(answer)  # 알파벳 순

# orders	course	result
# ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]	[2,3,4]	["AC", "ACDE", "BCFG", "CDE"]
# ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]	[2,3,5]	["ACD", "AD", "ADE", "CD", "XYZ"]
# ["XYZ", "XWY", "WXA"]	[2,3,4]	["WX", "XY"]