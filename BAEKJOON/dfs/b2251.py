# dfs !!! 물통
# bfs 사용해서 해결했다.
# visited는 a, b, c 모두에 대해서 만들 필요 없이, a, b가 결정되면 c도 결정되니 2차원으로 만들어도 충분하다
# a b c 각각에서 나머지 둘로 옮겨주는 경우를 하드 코딩했고, 물이 넘치거나 부족한 경우 등을 to에서 처리해줬다
from collections import deque

def bfs():
    q = deque()
    visited[0][0] = 1 # a, b에 물이 없을 때
    q.append((0, 0))
    ans = [C] # C에 가능한 물의 양
    while q:
        a, b = q.popleft()
        c = C - a - b # a, b가 결정되면 c도 자연스레 결정됨


        next = [0] * 6 # 가능한 모든 시행의 종류

        # to는 물이 넘치는 경우와 안 넘치는 경우를 모두 고려해줄 수 있다
        to = min(a+b, B) # a에서 b로 물을 옮길 때 a+b가 B보다 작으면 꽉 안차니 a+b, 그 외의 경우 꽉차니 B가 된다
        next[0] = (a+b-to, to, c) # a -> b

        to = min(a+c, C)
        next[1] = (a+c-to, b, to) # a -> c

        to = min(b + a, A)
        next[2] = (to, a + b - to, c) # b -> a

        to = min(b + c, C)
        next[3] = (a, b + c - to, to) # b -> c

        to = min(c + a, A)
        next[4] = (to, b, c + a - to) # c -> a

        to = min(c + b, B)
        next[5] = (a, to, c + b - to) # c -> b

        for v in next:
            v_a, v_b, v_c = v # 새롭게 변화한 물의 양

            if not visited[v_a][v_b]: # 만약 이전에 없었던 물 배열이라면 큐에 추가해줌
                visited[v_a][v_b] = 1
                q.append((v_a, v_b))

            if not v_a and v_c not in ans: # A가 비어있을 때 C에 가능한 물의 양을 고르는 문제다. C에 가능한 모든 물의 양의 종류를 맞추는 게 아니다. 이걸로 3번 정도 틀렸으니 문제를 잘 읽자...
                ans.append(v_c)
    else:
        ans.sort() # 오름차순
        print(*ans)

A, B, C = map(int, input().split())

visited = [[0]*(B+1) for _ in range(A+1)] # a에 가능한 물의 양 x b에 가능한 물의 양
bfs()


# 처음에 pour 함수 고민했다 실패한 흔적
# def pour(now, ind):
#     x = now[ind]
#     for i in range(3):
#
#
#
#     return (new_a1, new_b1, new_c1), (new_a2, new_b2, new_c2)
#
#
# def dfs(a, b, c):
#     visited[a][b] = 1
#     c = C - a - b
#     if a:
#         pour([a,b,c], 0)




    # q = deque()
    # visited[0][0] = 1
    # q.append((0, 0))
    # while q:
    #     a, b = q.popleft()
    #     c = C - a - b
    #
    #     for x in (a, b, c):
    #
    #         if x:
    #             if x >= B-b:
    #                 if not visited[x-(B-b)][B]:
    #                     q.append((x-(B-b), B))
    #                     visited[x-(B-b)][B] = 1
    #             else:
    #                 if not visited[0][x+b]:
    #                     q.append((0, x+b))
    #                     visited[0][x+b] = 1
    #
    #             if a >= C-c:
    #                 if not visited[a-(C-c)][B]:
    #                     q.append((a-(B-b), B))
    #                     visited[a-(B-b)][B] = 1
    #             else:
    #                 if not visited[0][a+b]:
    #                     q.append((0, a+b))
    #                     visited[0][a+b] = 1

