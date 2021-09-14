T = int(input()) # 테스트 케이스

for tc in range(1, T+1):
    N = int(input()) # 노드의 수
    LINE = [list(map(int, input().split())) for _ in range(N-1)] # 간선 정보
    A, B = list(map(int, input().split())) # 공통 조상 구할 두 노드
    adj_list = [[] for _ in range(N+1)] # 인접 리스트
    for line in LINE:
        adj_list[line[1]].append(line[0]) # 인접 리스트 생성

    a_list = [A] # A의 모든 조상 노드, A 포함
    a = A # 조상 노드 A부터 시작
    while adj_list[a]: # 부모가 있다면
        a = adj_list[a][0] # 부모가 새로운 a
        a_list.append(a) # 조상 노드 리스트에 부모 포함

    b = B # B의 가까운 조상부터 탐색해 나간다
    while b not in a_list: # B의 현재 조상이 A의 조상 노드 리스트에 포함
        b = adj_list[b][0] # 부모가 새로운 b
    print(b) # 가장 가까운 공통 조상