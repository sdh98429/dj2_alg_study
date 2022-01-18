# 2016년
# 12901

def solution(a, b):
    Month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    Day = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    answer = Day[(sum(Month[:a - 1]) + b) % 7]

    return answer

# a	b	result
# 5	24	"TUE"