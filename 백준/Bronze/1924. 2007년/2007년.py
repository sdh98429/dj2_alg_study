M, D = map(int, input().split())
MD = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
tot = 0
for m in range(0, M-1):
    tot += MD[m]
tot += D
DW = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
print(DW[tot%7])