def Erase(): # 지워지는 노드를 조상 노드로 가지는 모든 노드 제거
    global P, erase
    while True:
        flag = 1 # 지워지는 노드 추가 확인
        for i in range(N):
            if P[i] in erase: # 지워지는 노드들
                erase += [i] # 새로 지워지는 노드를 추가
                P[i] = -2 # 지워졌단 표시
                flag = 0 # 지워짐이 발생
        if flag: # 지워지는 노드가 더 이상 없다면 리턴
            return

N = int(input())
P = list(map(int, input().split()))
E = int(input())


l = [1] * N # 시작은 전부 리프 노드의 가능성이 있다고 봄
erase = [E] # 지워질 노드들

Erase() # 지우기

P[E] = -2 # -1과 겹치지 않는 독자적인 값
for i in range(N):
    if P[i] == -2: # 지워진 노드
        l[i] = 0 # 리프 노드 가능성 제거
    elif P[i] >= 0: # 루트 노트 -1 제외
        l[P[i]] = 0 # 남은 노드들 중 자식이 표시하는 부모 노드를 리프 노드 가능성 제거

print(sum(l)) # 리프노드의 합