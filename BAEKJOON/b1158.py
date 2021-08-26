from collections import deque

N, K = map(int, input().split())
q = deque([i + 1 for i in range(N)])
result = deque([])

k = 1
while q:
    if not k % K:
        result.append(q.popleft())
    else:
        q.append(q.popleft())
    k += 1
result = str(list(result))
print('<' + result[1:-1] + '>')