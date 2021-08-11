T = int(input())

meets = [0] * T

for tc in range(1, T+1):
    meets[tc-1] = list(map(int,input().split()))
result = 0
o_meets=sorted(meets, key=lambda x: x[0])
a = True
ind = 0
while len(o_meets):

    last = o_meets[0]
    plus = False
    for o_meet in o_meets:
        if (o_meet[1] <= last[1]):
            last = o_meet
            last_update = True
            plus = True
        if ((last[1] <= o_meet[0]) and last_update):
            next_start = ind
            last_update = False
        ind += 1
    if plus:
        result += 1
    o_meets = o_meets[next_start]
    try:
        if (o_meets[0] == last):
            o_meets.pop(0)
    except:
        pass
print(result)
