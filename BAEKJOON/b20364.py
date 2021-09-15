import sys

N, Q = list(map(int, sys.stdin.readline().split())) # 땅 개수 N, 오리 수 Q

house = [False] * (N+1) # 점유한 땅 리스트 house
for _ in range(Q): # 모든 오리에 대해
    A = int(sys.stdin.readline()) # 원하는 땅 번호 A
    a = A # 트리를 A부터 루트노드까지 타고 오른다(역방향)
    flag = False # 점유한 땅과 만났는지 여부 flag
    while a: # 노드의 번호가 1 이상인 경우, 즉 트리에 있는 경우
        if house[a]: # 현재 있는 노드가 이미 점유된 노드
            meet = a # 현재 역방향으로 추적 중이므로 루트 노드와 가까이에 있는 노드가 실제로 먼저 만난 노드 meet
            flag = True # 점유한 땅과 만남
        a //= 2 # 부모 노드로 현재 노드 변경
    if flag: # 만났다면
        print(meet) # 만난 노드 출력
    else: # 안만났다면
        house[A] = True # 원하는 노드 점유 표시
        print(0) # 원하는 노드에 왔으니 0 출력