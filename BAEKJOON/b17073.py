import sys
input = sys.stdin.readline # 이 코드 안 쓰면 시간 초과 납니다

N, W = map(int, input().split()) # 노드의 수 N, 고인 물의 양 W

adj_list = [[] for _ in range(N+1)] # 빈 인접 리스트

for _ in range(N-1):
    a, b = map(int, input().split()) #list 사용하면 시간 초과 잘 떠서 map으로 간선의 정보 받기
    adj_list[a].append(b) # 간선 방향성이 안 주어졌으므로 모든 경우의 수
    adj_list[b].append(a)

parent_list = [1] # 루트 노드
leaf_list = [1] * (N+1) # 모든 노드는 리프가 될 가능성 1 있음, N+1인 이유는 인덱싱 편하게

while parent_list: # 부모 노드가 존재할 때
    parent = parent_list.pop() # 부모 노드 리스트에서 부모 노드 꺼내기
    for child in adj_list[parent]: # 부모 노드에 연결된 노드 child
        if leaf_list[child]: # 만약 child가 leaf_list가 1, 즉 한 번 썼던 부모 노드가 아니라 리프가 될 가능성이 있다면
            leaf_list[parent] = 0 # 현재의 부모 노드는 리프가 될 자격이 없음
            parent_list.append(child) # 자식 노드 child가 부모 노드 리스트에 추가됨
print(W/(sum(leaf_list)-1)) # 물의 양의 기댓값은 (전체 물의 양/리프 노드의 개수), leaf_list N+1이니 1을 뺴줌
