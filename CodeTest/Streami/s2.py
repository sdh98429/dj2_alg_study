
# Example test:   '011100'
# OK
#
# Example test:   '111'
# OK
#
# Example test:   '1111010101111'
# OK
#
# Example test:
# OK

S = input()

def solution(S):
    W = list(S)
    ans = 0
    flag = False
    for w in W:
        if w == '1':
            flag = True

        if flag:
            if w == '1':
                ans += 2
            else:
                ans += 1

    return ans-1 if ans-1 >= 0 else 0


    # W = list(S)
    # V = 0
    # for ind in range(len(W)):
    #     V += 2 ** ind * int(W[len(W) - ind - 1])
    #
    # ans = 0
    # while V:
    #     if V%2:
    #         V -= 1
    #         ans += 1
    #     else:
    #         V //= 2
    #         ans += 1
    # return ans

print(solution(S))