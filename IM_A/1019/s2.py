T = int(input())

def nCm(ind, comb):
    global combination
    if len(comb) == 4:
        combination.append(comb)
        return
    if ind == N:
        return

    nCm(ind+1, comb)
    nCm(ind+1, comb+[ind])

for tc in range(1, T+1):
    N = int(input())
    user = list(map(int, input().split()))
    used = [0] * N
    combination = []
    nCm(0, [])
    max_num = 0
    for comb in combination:
        for i in range(4):
            if comb[i] - comb[i-1] in (1, N-1):
                break
        else:
            c1 = (user[comb[0]] + user[comb[1]]) ** 2 + (user[comb[2]] + user[comb[3]]) ** 2
            c2 = (user[comb[0]] + user[comb[3]]) ** 2 + (user[comb[1]] + user[comb[2]]) ** 2
            if max_num < max(c1, c2):
                max_num = max(c1, c2)
    print('#{} {}'.format(tc, max_num))


