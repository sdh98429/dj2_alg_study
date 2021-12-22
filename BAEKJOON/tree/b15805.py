# tree ! 트리 나라 관광 가이드
# 부모 도시 없다면 만들어주기

K = int(input())
A = list(map(int, input().split()))
N = max(A)

parent = [-2] * (N+1) # 루트 도시의 부모는 -1이니 존재하지 않는 값인 -2로 통일
parent[A[0]] = -1 # 루트 도시가 0번이 아닌 경우도 있다!
for i in range(K-1): # 만약 아직 부모가 없는 도시라면 바로 전 도시를 부모로 하기
    if parent[A[i+1]] == -2:
        parent[A[i+1]] = A[i]

print(N+1)
print(*parent)