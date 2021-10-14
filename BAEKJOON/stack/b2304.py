# stack 창고 다각형
# stack 사용하지 않고 앞으로 한 번, 뒤로 한 번 거쳐가며 계산
N = int(input())

def build(q):
    global tot
    max_ind, max_h = q[0]
    for i in range(N):
        ind, h = q[i]
        if h > max_h: # 더 높은 블록 만나면
            tot += max_h * abs(ind - max_ind) # 그 전까지의 블록 높이와 거리 차이 곱만큼 더하고
            max_h = h # 새롭게 최고 높이 블록 위치 등 갱신
            max_ind = ind
    return max_ind, max_h

store = [list(map(int, input().split())) for _ in range(N)]
store.sort()

tot = 0
max_ind1, max_h1 = build(store) # 앞에서 뒤로 최고 높이 블록 제외하고 순행
max_ind2, max_h2 = build(store[::-1]) # 역행
tot += (max_ind2 - max_ind1 + 1) * max_h1 # 최고 높이 블록만큼 더해줌, 두 개 이상인 경우도 포함

print(tot)






# max_H, max_I = sorted(store)[-1]
# store.sort()
# print(store)
#
# max_H1 = store[0][1]
# for ind, he in store:
#     if ind <= max_I