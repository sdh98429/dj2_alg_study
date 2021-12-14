# Example test:   ([1, 2, 4, 3], [1, 3, 2, 3])
# OK
#
# Example test:   ([3, 2, 1, 6, 5], [4, 2, 1, 3, 3])
# OK
#
# Example test:   ([1, 2], [1, 2])
# OK

def solution(A, B):
    N = len(A)
    space = [[] for _ in range(100001)]
    avail = [False] + [True] * (100000)
    for i in range(N):
        if i in space[A[i]]:
            avail[A[i]] = False
        space[A[i]].append(i)
        if i in space[B[i]]:
            avail[B[i]] = False
        space[B[i]].append(i)

    for i in range(100001):
        if avail[i]:
            return i
    else:
        return 100001



print(solution([1,2,3,3], [1,2,4,3]))