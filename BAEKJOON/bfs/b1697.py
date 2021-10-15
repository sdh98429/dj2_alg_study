
# bfs 숨바꼭질
# bfs로 전부 찾아가면 메모리 너무 크니 범위를 조절한다
def bfs():
    visited[N] = 0
    n = N
    q = []
    q.append(n)
    while q:
        n = q.pop(0)
        # 감소하는 방법은 1씩 감소하는 방법 뿐이므로 목적지가 현재보다 작으면 그 차이만큼 더해줌
        if n >= K:
            if visited[K] >= visited[n] + (n-K):
                visited[K] = visited[n] + (n-K)
        else:
            # -1만큼 이동, +1 만큼 이동, *2 만큼 이동
            for w in (n-1, n+1, n*2):
                # w가 범위 안에 있고 w의 visited가 현재에 1 더해준것보다 작으면
                if w in range(limit) and visited[w] > visited[n] + 1:
                    q.append(w)
                    visited[w] = visited[n] + 1




N, K = map(int, input().split())
# 쓸데없이 큰 행렬이 만들어지는 것을 방지하고, 어차피 목적지의 2배 이상의 크기 되면 그 이후론 visited가 커질 뿐이다.
# 끝에 100000 가 아니라 100001로 마지막 숫자를 포함해야하는 것에 유념! 전자로 하면 오류난다.
limit = 2 * max(N, K) + 1 if 100000 > 2 * max(N, K) else 100001
visited = [987654321] * (limit +1)
bfs()
print(visited[K])