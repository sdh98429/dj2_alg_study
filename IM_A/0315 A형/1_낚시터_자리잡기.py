# !!! 낚시터 자리잡기, 마지막 사람 else에서 dfs로 두 가지 경우 타고가기

min_dist = 987654321

def dfs(used, DS, SP, F, N):
    global min_dist

    if sum(used) == 3:
        if min_dist > DS:
            min_dist = DS
        return

    for ind in range(3):
        if not used[ind]:
            used[ind] = True
            loc = F[ind][0]
            fisher = F[ind][1]
            dist = DS
            space = SP.copy()
            for _ in range(fisher-1):
                for i in range(N):
                    if (loc+i) in range(1, N+1) and not space[loc+i]:
                        space[loc+i] = True
                        dist += i+1
                        break
                    elif (loc-i) in range(1, N+1) and not space[loc-i]:
                        space[loc-i] = True
                        dist += i+1
                        break
            else:
                flag = False
                for i in range(N):
                    if (loc+i) in range(1, N+1) and not space[loc+i]:
                        space[loc+i] = True
                        flag = True
                        dfs(used, dist+i+1, space, F, N)
                    if (loc-i) in range(1, N+1) and not space[loc-i]:
                        space[loc-i] = True
                        flag = True
                        dfs(used, dist+i+1, space, F, N)
                    if flag:
                        break
            
            used[ind] = False



T = int(input())

for tc in range(1, T + 1):
    min_dist = 9877654321
    N = int(input())
    Space = [True] + [False] * N
    F = []
    used = [False] * 3
    for _ in range(3):
	    F.append(list(map(int, input().split())))

    dfs(used, 0, Space, F, N)
    print("#%d" %tc, end=" ")
    print(min_dist)