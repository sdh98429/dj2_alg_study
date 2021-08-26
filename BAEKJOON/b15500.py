from collections import deque

N = int(input())
q = [[] for _ in range(3)]
q[0] = list(map(int, input().split()))
q[1] = []
q[2] = []
result = []
n = N
K = 0
while len(q[2]) < N:
    if n in q[0]:
        while q[0][-1] != n:
            q[1].append(q[0].pop())
            result.append('1 2')
            K += 1
        q[2].append(q[0].pop())
        result.append('1 3')
        K += 1
    else:
        while q[1][-1] != n:
            q[0].append(q[1].pop())
            result.append('2 1')
            K += 1
        q[2].append(q[1].pop())
        result.append('2 3')
        K += 1
    n -= 1
print(K)
for ind in range(K):
    print(result[ind])