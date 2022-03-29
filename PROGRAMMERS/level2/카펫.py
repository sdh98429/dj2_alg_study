# ! 카펫
# 42842

def solution(brown, yellow):
    b = -(brown-4)/2 # x1 + x2
    c = yellow # x1 * x2
    x1 = (-b+((b**2-4*c)**(1/2)))/2 # 2차 방정식 큰 해
    x2 = (-b-((b**2-4*c)**(1/2)))/2 # 2차 방정식 작은 해

    return [x1+2, x2+2]

# brown	yellow	return
# 10	2	[4, 3]
# 8	1	[3, 3]
# 24	24	[8, 6]