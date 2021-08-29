N = int(input())

def prime(num, val):
    global mir_p
    for s in range(2, int(num ** 1/2) + 1):
        if not num % s:
            return
    else:
        mir_p[val] += [num]

def miracle(place):
    global mir_p
    for n in range(2, place + 1):
        for mir in mir_p[n-1]:
            for i in [1, 3, 5, 7, 9]:
                prime(10 * mir + i, n)


mir_p = [[] for _ in range(9)]
mir_p[1] = [2, 3, 5, 7]

miracle(N)
for i in range(len(mir_p[N])):
    print(mir_p[N][i])